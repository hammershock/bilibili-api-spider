"""
接口返回值类型见bili_api/response_demo/
或者TypeHint
"""

from bili_api import get_info, get_video_tags, get_video_pages, get_subtitles, get_user_access_details


if __name__ == '__main__':
    cookie = ...  # 替换为你的b站cookies, 或者将cookies写入bilibili_api/cookies.txt

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
    subtitles = get_subtitles(subtitle_url, cookie)
    print(subtitles)
