import functools
import re

data = open('inputs/day4.txt').read().splitlines()

# Parse data
passports = [dict()]
for line in data:
    if len(line) > 0:
        d = passports[-1]
        for pair in line.split(" "):
            key, val = pair.split(":")
            d[key] = val
    else:
        passports.append(dict())


def valid_part1(passport):
    with_cid = ('cid' in passport) and (len(passport.keys()) == 8)
    without_cid = ('cid' not in passport) and (len(passport.keys()) == 7)
    return with_cid or without_cid


def between(val, min, max):
    return int(val) >= min and int(val) <= max


def hgt_valid(hgt):
    return ('cm' in hgt and between(hgt[:-2], 150, 193)) or ('in' in hgt and between(hgt[:-2], 59, 76))


def valid_part2(pp):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    byr = 'byr' in pp and between(pp['byr'], 1920, 2002)
    iyr = 'iyr' in pp and between(pp['iyr'], 2010, 2020)
    eyr = 'eyr' in pp and between(pp['eyr'], 2020, 2030)
    hgt = 'hgt' in pp and hgt_valid(pp['hgt'])
    hcl = 'hcl' in pp and re.match(r"^#[0-9a-f]{6}", pp['hcl'])
    ecl = 'ecl' in pp and pp['ecl'] in colors
    pid = 'pid' in pp and len(pp['pid']) == 9 and pp['pid'].isdigit()
    return byr and iyr and eyr and hgt and hcl and ecl and pid


print('Answer part 1: ', len(filter(valid_part1, passports)))
print('Answer part 2: ', len(filter(valid_part2, passports)))
