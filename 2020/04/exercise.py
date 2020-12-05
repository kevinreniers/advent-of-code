def update_passport(passport=None, info={}):
    if passport is None:
        passport = {'byr': None,'iyr': None,'eyr': None,'hgt': None, 'hcl': None, 'ecl': None, 'pid': None, 'cid': None }
    passport.update(info)
    return passport


def is_valid_passport(passport: dict):
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    print('keys', passport.keys())
    for r in req:
        if passport.get(r, None) is None:
            return False
    return True


def valid_passport_count(data):
    is_valid = 0
    is_invalid = 0
    passport = None
    while lines:
        line = lines.pop().rstrip()
        print(line)
        if line == '':
            if is_valid_passport(passport):
                is_valid += 1
            else:
                is_invalid += 1
            passport = None
            continue
        cols = line.split(' ')
        x = [col.split(':') for col in cols]
        passport = update_passport(passport, x)
    is_valid += int(is_valid_passport(passport))
    print((is_valid, is_invalid))
    return is_valid

with open('test.txt', 'r') as f:
    lines = [l for l in f]

assert(valid_passport_count(lines) == 2)

with open('data.txt', 'r') as f:
    lines = [l for l in f]

print(valid_passport_count(lines))