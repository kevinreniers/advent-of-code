def count_is_valid(filename, func):
    with open(filename, 'r') as f:
        lines = [d for d in f]
    
    return sum(int(func(ans)) for ans in lines)

def parse(line):
    policy, password = str(line).split(':')
    criteria, char = policy.split(' ')
    first, second = criteria.split('-')
    return int(first), int(second), char, password

def min_max_occurrences(line):
    f, s, c, p = parse(line)
    return f <= p.count(c) <= s

def xor_char(line):
    f, s, c, p = parse(line)
    return bool(p[f] == c) ^ bool(p[s] == c)           

assert(count_is_valid('test.txt', min_max_occurrences) == 2)
assert(count_is_valid('test.txt', xor_char) == 1)

print(count_is_valid('data.txt', min_max_occurrences))  # 640
print(count_is_valid('data.txt', xor_char))  # 472