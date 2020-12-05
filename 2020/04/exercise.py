import re

def update_passport(passport=None, info={}):
    if passport is None:
        passport = {'byr': None,'iyr': None,'eyr': None,'hgt': None, 'hcl': None, 'ecl': None, 'pid': None, 'cid': None }
    passport.update(info)
    return passport


def str_(val):
    return '' if val is None else str(val)



def passport_has_required_fields(passport: dict):
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for r in req:
        if passport.get(r, None) is None:
            return False
    return True


def is_valid_passport(passport: dict):
    print('validating', passport)

    byr = str_(passport.get('byr', None))
    if byr == '' or not byr.isnumeric() or not (1920 <= int(byr) <= 2002):
        print('byr', byr)
        return False
    
    iyr = str_(passport.get('iyr', None))
    if iyr == '' or not iyr.isnumeric() or not (2010 <= int(iyr) <= 2020):
        print('iyr', iyr)
        return False
    
    eyr = str_(passport.get('eyr', None))
    if eyr == '' or not eyr.isnumeric() or not (2020 <= int(eyr) <= 2030):
        print('eyr', eyr)
        return False
    
    hgt = str_(passport.get('hgt', None))
    if not hgt.endswith('cm') and not hgt.endswith('in'):
        print('hgt')
        return False
    else:
        if hgt.endswith('cm') and not (150 <= int(hgt[0:-2]) <= 193):
            print('hgt cm', hgt)
            return False
        elif hgt.endswith('in') and not (59 <= int(hgt[0:-2]) <= 76):
            print('hgt in', hgt)
            return False

    hcl = str_(passport.get('hcl', None))
    if not re.search(r'^#[0-9a-f]{6}$', hcl):
        print('hcl', hcl)
        return False
    
    ecl = str_(passport.get('ecl', None))
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('ecl', ecl)
        return False
    
    pid = str_(passport.get('pid', None))
    if not re.search(r'^\d{9}$', pid):
        print('pid', pid)
        return False

    print('valid')
    return True

def valid_passport_count(data, validator):
    is_valid = 0
    is_invalid = 0
    passport = None
    while lines:
        line = lines.pop().rstrip()
        if line == '':
            if validator(passport):
                is_valid += 1
            else:
                is_invalid += 1
            passport = None
            continue
        cols = line.split(' ')
        x = [col.split(':') for col in cols]
        passport = update_passport(passport, x)
    is_valid += int(validator(passport))
    print((is_valid, is_invalid))
    return is_valid

with open('test.txt', 'r') as f:
    lines = [l for l in f]

assert(valid_passport_count(lines, passport_has_required_fields) == 2)

with open('data.txt', 'r') as f:
    lines = [l for l in f]

print(valid_passport_count(lines, is_valid_passport))