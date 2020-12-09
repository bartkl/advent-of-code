from pprint import pprint
from string import hexdigits


PASSPORT_FILE = 'data/passports.txt'

MANDATORY_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


class Validator:
    @staticmethod
    def byr(v):
        return v.isdigit() and 1920 <= int(v) <= 2002

    @staticmethod
    def iyr(v):
        return v.isdigit() and 2010 <= int(v) <= 2020

    @staticmethod
    def eyr(v):
        return v.isdigit() and 2020 <= int(v) <= 2030

    @staticmethod
    def hgt(v):
        unit = v[-2:]
        measurement = v[:-2]

        if unit == 'cm' and measurement.isdigit():
            return 150 <= int(measurement) <= 193
        elif unit == 'in' and measurement.isdigit():
            return 59 <= int(measurement) <= 76
        else:
            return False

    @staticmethod
    def hcl(v):
        return v.startswith('#') and all(c in hexdigits for c in v[1:]) and len(v) == 7

    @staticmethod
    def ecl(v):
        return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    @staticmethod
    def pid(v):
        return v.isdigit() and len(v) == 9


if __name__ == '__main__':
    valid_passport_count = 0
    with open(PASSPORT_FILE) as f:
        passports_str = f.read()

    passports = passports_str.split('\n\n')

    passports = [dict([e.split(':') for e in p.split()]) for p in passports]

    for p in passports:
        valid = True
        for field in MANDATORY_FIELDS:
            if field not in p:
                valid = False
            else:
                validator = getattr(Validator, field)
                valid = validator(p[field])

            if not valid:
                break

        if valid:
            valid_passport_count += 1

    print(valid_passport_count)


