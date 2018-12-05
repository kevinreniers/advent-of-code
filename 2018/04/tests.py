from random import shuffle
from solution import log_sort, log_parse, log_sleep_parser

pattern = [
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-03 00:29] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-05 00:55] wakes up",
]

shuffled_pattern = pattern.copy()
shuffle(shuffled_pattern)


def guard_is_sorted(logs):
    previous = 0
    for log in logs:
        timestamp = int(log)
        assert timestamp > previous
        previous = timestamp


if __name__ == '__main__':
    sorted_logs = log_sort(log_parse(shuffled_pattern))
    parsed_logs = log_parse(pattern)

    # assert that logs are sorted from oldest to newest
    guard_is_sorted(parsed_logs)
    guard_is_sorted(sorted_logs)

    guards = log_sleep_parser(sorted_logs)

    # assert some facts (from the example)
    assert guards.sleepiest_guard.id == '10'
    assert guards.sleepiest_guard.total_sleep == 50
    assert len(guards.guards) == 2
    assert guards.sleepiest_guard.sleepiest_minute_id() == 240
    assert guards.strategy2().sleepiest_minute_id() == 4455

