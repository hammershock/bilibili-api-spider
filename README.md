# bilibili-api-spider (Archived)

> **This project has been superseded by [bilicli](https://github.com/hammershock/bilibili-cli) — a full-featured, read-only Bilibili CLI tool for terminal and agent use.**
>
> `bilicli` provides everything this project did and much more: QR code login, video/user search, feed, subtitles, danmaku, comments, multi-part video support, audio download, cover download, and local speech-to-text transcription — all from a single `pip install`.
>
> **Please use [hammershock/bilibili-cli](https://github.com/hammershock/bilibili-cli) instead.**

---

## Original Description

与获取BILIBILI视频信息有关的爬虫+API访问

这个项目提供了一个通过UP主ID获取全部发布视频信息，以及根据视频号(BVID)获取视频信息，如播放量，点赞数，视频字幕等。

### Why bilicli?

| Feature | bilibili-api-spider | bilicli |
|---------|-------------------|---------|
| Login | Manual cookie extraction | QR code scan |
| Browser dependency | Requires Chrome + ChromeDriver | None |
| Install | Manual dependency management | `pip install -e .` |
| Video info | Basic API calls | Full CLI with `--json` output |
| Multi-part videos | Manual CID extraction | `bilicli pages` + `--page N` |
| Subtitles | Manual URL construction | `bilicli subtitle` |
| Download | Not supported | Video, audio, cover |
| Comments | Not supported | Comments + replies with pictures |
| Search | Not supported | Video and user search |
| Agent-friendly | No | `--json`, `--quiet`, pagination hints |
| Transcription | No | Local mlx-whisper STT |
