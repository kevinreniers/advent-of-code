import re
from collections import namedtuple, OrderedDict

Log = namedtuple('Log', ['year', 'month', 'day', 'hour', 'minute', 'id'])


def log_parse(logs: list):
    matched_logs = {}
    pattern = re.compile(
        '\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (Guard #(\d+) begins shift|falls asleep|wakes up)')
    for log in logs:
        match = pattern.match(log)
        log_key = '{}{}{}{}{}'.format(match[1], match[2], match[3], match[4], match[5])
        matched_logs[log_key] = Log(match[1], match[2], match[3], match[4], match[5], match[6])
    return matched_logs


def log_sort(parsed_logs):
    return OrderedDict(sorted(parsed_logs.items(), key=lambda t: t[0]))
