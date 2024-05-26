import os.path


COOKIE_PATH = os.path.join(os.path.dirname(__file__), 'cookies.txt')


def make_header(cookie=None):
    if cookie is None:
        if not os.path.exists(COOKIE_PATH):
            raise FileNotFoundError('Cookie file not found')
        with open(COOKIE_PATH, 'r') as f:
            cookie = f.read().strip()
    return {
        'authority': 'api.bilibili.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'cookie': cookie
    }
