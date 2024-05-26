# -*- coding: utf-8 -*-
"""
获取用户全部投稿视频信息
"""

import os
from bili_spider import make_chrome_browser, get_user_videos


if __name__ == '__main__':
    mid = 1629347259  # 用户id

    with make_chrome_browser(executable_path="./chromedriver", headless=False) as browser, open("info.txt", "w") as f:
        for attrs in get_user_videos(browser, mid):
            f.write("\t".join(attrs) + '\n')
        os.rename("info.txt", f"{attrs[2]}.txt")
