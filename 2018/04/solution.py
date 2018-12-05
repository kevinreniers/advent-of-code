import re
from collections import OrderedDict
import operator


class Log(object):
    def __init__(self, year, month, day, hour, minute, guard, log):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.log = log
        self.guard = guard

    def is_shift_started(self):
        return self.guard is not None

    def is_awake(self):
        return self.log == 'wakes up'

    def is_asleep(self):
        return self.log == 'falls asleep'


def log_parse(logs: list):
    matched_logs = {}
    pattern = re.compile(
        '\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\](?: Guard #(\d+))? (begins shift|falls asleep|wakes up)')
    for log in logs:
        match = pattern.match(log)
        log_key = '{}{}{}{}{}'.format(match[1], match[2], match[3], match[4], match[5])
        matched_logs[log_key] = Log(match[1], match[2], match[3], match[4], match[5], match[6], match[7])
    return matched_logs


def log_sort(parsed_logs):
    ordered_dict = OrderedDict(sorted(parsed_logs.items(), key=lambda t: t[0]))
    return ordered_dict


class Guard(object):
    def __init__(self, guard_id):
        self.asleep_at = 0
        self.awake_at = 0
        self.id = guard_id
        self.total_sleep = 0
        self.sleep_minutes = {}

    def calc_sleep(self, sleep_from: int, sleep_until: int):
        diff = sleep_until - sleep_from
        self.total_sleep += diff
        for minute in range(sleep_from, sleep_until):
            self.sleep_minutes[minute] = self.sleep_minutes.get(minute, 0) + 1

    def sleep(self, minute):
        self.asleep_at = minute

    def wake_up(self, minute):
        self.calc_sleep(self.asleep_at, minute)

    def sleepiest_minute(self):
        # print(self.id, self.sleep_minutes)
        if len(self.sleep_minutes) != 0:
            return max(self.sleep_minutes.items(), key=operator.itemgetter(1))[0]

    def sleepiest_minute_count(self):
        if self.sleepiest_minute() is None:
            return 0
        return self.sleep_minutes[self.sleepiest_minute()]

    def sleepiest_minute_id(self):
        if self.sleepiest_minute() is None:
            return 0
        return int(self.id) * self.sleepiest_minute()


class Guards(object):
    def __init__(self):
        self.guards = {}
        self.sleepiest_guard = None

    def get_guard(self, guard_id: int):
        return self.guards.get(guard_id, Guard(guard_id))

    def touch(self, guard: Guard):
        self.guards[guard.id] = self.guards.get(guard.id, guard)
        if self.sleepiest_guard is None:
            self.sleepiest_guard = self.guards[guard.id]

        if self.sleepiest_guard.total_sleep < self.guards[guard.id].total_sleep:
            self.sleepiest_guard = self.guards[guard.id]

    def strategy2(self):
        sleepiest_count = 0
        sleepiest_guard = None
        for id, guard in self.guards.items():
            if guard.sleepiest_minute_count() > sleepiest_count:
                sleepiest_guard = guard
                sleepiest_count = guard.sleepiest_minute_count()
        return sleepiest_guard


def log_sleep_parser(logs):
    guards = Guards()
    guard = None

    for key in logs:
        log = logs[key]
        if log.is_shift_started():
            if guard is not None:
                guards.touch(guard)
            guard = guards.get_guard(log.guard)
            continue

        if log.is_asleep():
            guard.sleep(log.minute)
            continue

        if log.is_awake():
            guard.wake_up(log.minute)
            continue
    return guards


def calc_sleepiest_guard(guard_stats):
    guard_id = None
    sleepiest_guard = None
    total = 0
    for guard in guard_stats:
        guard_total = guard_stats[guard]['total']
        if guard_total > total:
            sleepiest_guard = guard_stats[guard]
            guard_id = guard
            total = guard_total
    return guard_id, sleepiest_guard


if __name__ == '__main__':
    with open(r'in.txt') as file:
        unsorted_logs = file.readlines()
    sorted_logs = (log_sort(log_parse(unsorted_logs)))
    sleepy_guards = log_sleep_parser(sorted_logs)
    print('Result of Part 1: ', sleepy_guards.sleepiest_guard.sleepiest_minute_id())
    sleepiest_minute_dude = sleepy_guards.strategy2()
    print(sleepiest_minute_dude.id, sleepiest_minute_dude.sleepiest_minute(),
          sleepiest_minute_dude.sleepiest_minute_count())
    print('Result of Part 2: ', sleepiest_minute_dude.sleepiest_minute_id())
