import re

REGEX = re.compile(r'([a-z]+):([a-zA-z0-9#]+)')  # https://pythex.org/

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
        return True

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
