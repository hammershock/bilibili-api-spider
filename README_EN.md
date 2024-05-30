# Bilibili Video Information Crawler + API Access

This project provides a way to retrieve all published video information by UP master ID and get video information such as play count, likes, video subtitles, etc., by video number (BVID).

[![requests](https://img.shields.io/badge/requests-2.32.2-2D9CDB?logo=pypi)](https://pypi.org/project/requests/)
[![bs4](https://img.shields.io/badge/bs4-0.0.2-2D9CDB?logo=pypi)](https://pypi.org/project/bs4/)
[![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-4.12.3-2D9CDB?logo=pypi)](https://pypi.org/project/beautifulsoup4/)
[![selenium](https://img.shields.io/badge/selenium-4.21.0-2D9CDB?logo=pypi)](https://pypi.org/project/selenium/)
[![tqdm](https://img.shields.io/badge/tqdm-4.66.4-2D9CDB?logo=pypi)](https://pypi.org/project/tqdm/)

## Main Features:
- Retrieve all video information published by UP master
- Get detailed video information, including video subtitles

## Dependencies

```bash
pip install selenium bs4 requests
pip install tqdm
```

## Usage
Example 1: Retrieve all video information by UP master:

Directly access the API, and it's easier to succeed by using cookies. Cookies can be obtained by logging into Bilibili and using `F12` -> `Network` to monitor communication with Bilibili.
You can pass cookies when calling the interface or write cookies into `bili_api/cookie.txt`.

Note: Abusing the API may temporarily disable the corresponding API functionality!
All methods for accessing the API to get video information are in `bili_api`. [Detailed return value example](bili_api/response_demo)

```python
import os
from bili_spider import make_chrome_browser, get_user_videos

if __name__ == '__main__':
    mid = 1629347259  # User ID

    with make_chrome_browser(executable_path="./chromedriver", headless=False) as browser, open("info.txt", "w") as f:
        for attrs in get_user_videos(browser, mid):  # Get all video attributes of a specific mid user, all types are strings
            f.write("\t".join(attrs) + '\n')
            # Video URL, video BV number, username, video title, play count, release date, video duration
            url, bvid, user_name, title, num_plays, pub_datetime, duration = attrs
            UP_name = attrs[2]
        os.rename("info.txt", f"{UP_name}.txt")  # Save the result to {UP_name}.txt
```

Example 2: Get detailed video information:

You need to use `selenium` to crawl, then install `chrome` and the corresponding version of `chrome driver`. Note that the version number before the first dot must match.

```python
from bili_api import get_info, get_video_tags, get_video_pages, get_subtitles_from_url, get_user_access_details

if __name__ == '__main__':
    cookie = None  # Replace with your Bilibili cookies, or write cookies into bili_api/cookies.txt

    bvid = "BV1Yz421a7iJ"
    info = get_info(bvid, cookie)
    print("info", info)

    tags = get_video_tags(bvid, cookie)
    print(tags)

    pages = get_video_pages(bvid, cookie)
    print(pages)

    cid = pages[0]['cid']  # The CID of the first video part
    details = get_user_access_details(bvid, cid, cookie)
    print(details)

    subtitle_url = "https:" + details["subtitle"]["subtitles"][0]['subtitle_url']
    subtitles = get_subtitles_from_url(subtitle_url, cookie)
    print(subtitles)
```

Make sure to replace the example values with actual data and your specific requirements when using this code.
