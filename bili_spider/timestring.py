from datetime import datetime, timedelta
import re


def parse_timestring(timestring: str) -> datetime:
    now = datetime.now()

    patterns = [
        (r"刚刚", lambda m: now),  # 刚刚
        (r"(\d+)分钟前", lambda m: now - timedelta(minutes=int(m.group(1)))),
        (r"(\d+)小时前", lambda m: now - timedelta(hours=int(m.group(1)))),
        (r"昨天", lambda m: now - timedelta(days=1)),
        (r"(\d+)-(\d+)-(\d+)", lambda m: datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))),
        (r"(\d+)-(\d+)", lambda m: datetime(now.year, int(m.group(1)), int(m.group(2))))
    ]

    for pattern, handler in patterns:
        if match := re.match(pattern, timestring):
            return handler(match)

    raise ValueError(f"Unsupported timestring format: {timestring}")


if __name__ == '__main__':
    print(parse_timestring("3分钟前"))
    print(parse_timestring("8小时前"))
    print(parse_timestring("12小时前"))
    print(parse_timestring("昨天"))
    print(parse_timestring("5-24"))  # 默认今年
    print(parse_timestring("2021-3-18"))
