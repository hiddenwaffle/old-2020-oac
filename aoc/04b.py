import re

REGEX = re.compile(r'([a-z]+):([a-zA-z0-9#]+)')  # https://pythex.org/
HGT_REGEX = re.compile(r'(\d+)(cm|in)')
HCL_REGEX = re.compile(r'#([a-f]|\d){6}')

# NOTE: cid is optional (1/2)
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


class Passport:
    def __init__(self):
        self.fields = {}
        self.count = 0

    def line_into_fields(self, line):
        matches = REGEX.findall(line)
        for field, value in matches:
            if field not in REQUIRED_FIELDS and field != 'cid':  # NOTE: cid is optional (2/2)
                raise Exception(field)
            self.fields[field] = value
            self.count += 1

    def valid(self):
        for required_field in REQUIRED_FIELDS:
            if required_field not in self.fields:
                return False
        # Additional validation
        # -------------------------------- byr
        if len(self.fields['byr']) != 4:
            return False
        byr = int(self.fields['byr'])
        if byr < 1920 or byr > 2002:
            return False
        # --------------------------------iyr
        if len(self.fields['iyr']) != 4:
            return False
        iyr = int(self.fields['iyr'])
        if iyr < 2010 or iyr > 2020:
            return False
        if len(self.fields['eyr']) != 4:
            return False
        # --------------------------------eyr
        eyr = int(self.fields['eyr'])
        if eyr < 2020 or eyr > 2030:
            return False
        # --------------------------------hgt
        if not self.valid_hgt():
            return False
        # --------------------------------hcl
        if not HCL_REGEX.match(self.fields['hcl']):
            return False
        # --------------------------------ecl
        if not self.fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        # --------------------------------pid
        if len(self.fields['pid']) != 9:
            return False
        try:
            int(self.fields['pid'])
        except ValueError:
            return False
        return True

    def valid_hgt(self):
        match = HGT_REGEX.match(self.fields['hgt'])
        if match:
            num = int(match.group(1))
            measure = match.group(2)
            if measure == 'cm' and (num < 150 or num > 193):
                return False
            elif measure == 'in' and (num < 59 or num > 76):
                return False
            elif measure not in ['cm', 'in']:
                return False
            return True
        return False

    def __str__(self):
        return str(self.fields)


def main():
    with open('input/04.data') as file:
        lines = file.read().splitlines()
    valid = 0
    passport = Passport()
    for line in lines:
        line = line.strip()
        if line:
            passport.line_into_fields(line)
        else:
            if passport.valid():
                valid += 1
            passport = Passport()
    # Prevent off-by-one, took forever to figure out
    if passport.valid():
        valid += 1
    print(valid)


if __name__ == '__main__':
    main()
