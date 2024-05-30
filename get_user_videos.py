# -*- coding: utf-8 -*-
"""
获取用户全部投稿视频信息
"""

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
