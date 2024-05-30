# 与获取BILIBILI视频信息有关的爬虫+API访问

这个项目提供了一个通过UP主ID获取全部发布视频信息，以及根据视频号(BVID)获取视频信息，如播放量，点赞数，视频字幕等。

[![requests](https://img.shields.io/badge/requests-2.32.2-blue)](https://pypi.org/project/requests/)
[![bs4](https://img.shields.io/badge/bs4-0.0.2-blue)](https://pypi.org/project/bs4/)
[![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-4.12.3-blue)](https://pypi.org/project/beautifulsoup4/)
[![selenium](https://img.shields.io/badge/selenium-4.21.0-blue)](https://pypi.org/project/selenium/)
[![tqdm](https://img.shields.io/badge/tqdm-4.66.4-blue)](https://pypi.org/project/tqdm/)

## 主要功能：
- 获取UP主发布的所有视频信息
- 获取视频的详细视频信息，视频字幕

## 依赖

```bash
pip install selenium bs4 requests
pip install tqdm
```

## 使用方法
eg.1 获取UP主所有视频信息:

直接通过api访问，注意要使用cookies才更容易成功
cookies可以在登陆b站后，在网页通过`F12`-`网络` 监听与bilibili的通信获得
可以在每次调用接口时传入cookies，也可以将cookies写入`bili_api/cookie.txt`

注意: api滥用会导致对应api功能暂时封禁！！
所有访问api获取视频信息的方法在`bili_api`中，[详细返回值示例](bili_api/response_demo)

```python
import os
from bili_spider import make_chrome_browser, get_user_videos


if __name__ == '__main__':
    mid = 1629347259  # 用户id

    with make_chrome_browser(executable_path="./chromedriver", headless=False) as browser, open("info.txt", "w") as f:
        for attrs in get_user_videos(browser, mid):  # 获取特定mid用户的全部视频属性,类型均为字符串
            f.write("\t".join(attrs) + '\n')
            # 视频url，视频bv号，用户名，视频标题，播放量，发布日期，视频时长
            url, bvid, user_name, title, num_plays, pub_datetime, duration = attrs
            UP_name = attrs[2]
        os.rename("info.txt", f"{UP_name}.txt")  # 将结果保存至{UP_name}.txt
```
eg.2 获取视频详细信息:

需要用到`selenium`爬取
然后安装`chrome`和对应版本的`chrome driver`，注意第一个点之前的版本号一定要对应

```python
from bili_api import get_info, get_video_tags, get_video_pages, get_subtitles_from_url, get_user_access_details


if __name__ == '__main__':
    cookie = None  # 替换为你的b站cookies, 或者将cookies写入bilibili_api/cookies.txt

    bvid = "BV1Yz421a7iJ"
    info = get_info(bvid, cookie)
    print("info", info)

    tags = get_video_tags(bvid, cookie)
    print(tags)

    pages = get_video_pages(bvid, cookie)
    print(pages)

    cid = pages[0]['cid']  # 第一个分P的cid
    details = get_user_access_details(bvid, cid, cookie)
    print(details)

    subtitle_url = "https:" + details["subtitle"]["subtitles"][0]['subtitle_url']
    subtitles = get_subtitles_from_url(subtitle_url, cookie)
    print(subtitles)

```
