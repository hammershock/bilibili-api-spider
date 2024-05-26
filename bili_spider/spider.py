import os.path
import random
import time
from contextlib import contextmanager
from typing import Generator, Tuple

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm

from .timestring import parse_timestring

api_user = 'https://space.bilibili.com/{}/video?tid=0&pn={}&keyword=&order=pubdate'


@contextmanager
def make_chrome_browser(executable_path=None, headless=True):
    """

    :param executable_path: chrome driver path
    :return:
    """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    service = Service(executable_path=executable_path)
    browser = webdriver.Chrome(options=options, service=service)
    try:
        yield browser
    finally:
        browser.quit()


def __get_user_videos(browser, mid: int, page: int = 1, p_bar=None, user_name=None):
    browser.get(api_user.format(mid, page))
    time.sleep(1 + 2 * random.random())
    html = BeautifulSoup(browser.page_source, features="html.parser")
    num_page = 0

    if page == 1:
        total_pages = html.find('span', attrs={'class': 'be-pager-total'}).text  # 共 88 页，
        user_name = html.find('span', id='h-name').text  # 红警HBK08
        num_page = int(total_pages.split(' ')[1])  # 88
        p_bar = tqdm(total=num_page, desc=f"grabbing user {user_name}")

    ul_data = html.find('div', id='submit-video-list').find('ul', attrs={'class': 'clearfix cube-list'})
    p_bar.set_postfix(page=page)
    for li in ul_data.find_all('li'):
        a = li.find('a', attrs={'target': '_blank', 'class': 'title'})
        url = 'https:{}'.format(a['href'])  # 'https://www.bilibili.com/video/BV1ws421g7Tw/'
        bvid = url.strip("/").split("/")[-1]
        title = a.text  # '红警基地车引诱一下！对手果然上当，全歼敌军坦克！'
        pub_date_string = li.find('span', attrs={'class': 'time'}).text.strip()  # '5小时前'
        pub_datetime = parse_timestring(pub_date_string)
        num_plays = li.find('span', attrs={'class': 'play'}).text.strip()  # '10.8万'
        duration = li.find('span', attrs={'class': 'length'}).text.strip()  # '11:02'
        yield url, bvid, user_name, title, num_plays, str(pub_datetime), duration

    p_bar.update(1)
    if page == 1:
        for page_i in range(2, num_page + 1):
            for attrs in __get_user_videos(browser, mid, page_i, p_bar, user_name=user_name):
                yield attrs


def get_user_videos(browser, mid: int) -> Generator[Tuple[str, str, str, str, str, str, str], None, None]:
    """
    获取user发布的所有视频信息需要通过selenium动态执行script获取，无法通过api访问直接获得
    >>> mid = 1629347259
    >>> executable_path = os.path.join(os.path.dirname(__file__), 'chromedriver')
    >>> with make_chrome_browser(executable_path) as browser:
    ...    for url, bvid, user_name, title, num_plays, pub_date, duration in get_user_videos(browser, mid):
    ...        pass

    :param browser: browser instance
    :param mid: 创作者id（UP主用户id）
    :return:
    """
    return __get_user_videos(browser, mid)
