import re

REGEX = re.compile(r'([a-z]+):([a-zA-z0-9#]+)')  # https://pythex.org/

# NOTE: Not requiring cid
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


class Passport:
    def __init__(self):
        self.fields = {}

    def line_into_fields(self, line):
        matches = REGEX.findall(line)
        for field, value in matches:
            if field not in REQUIRED_FIELDS and field != 'cid':  # NOTE: cid is optional
                raise Exception(field)
            self.fields[field] = value

    def set(self, field, value):
        self.fields[field] = value

    def valid(self):
        for field in REQUIRED_FIELDS:
            if field not in self.fields:
                return False
        return True


def main():
    with open('input/04.data') as file:
        lines = file.read().splitlines()
    valid = 0
    passport = Passport()
    for i in range(len(lines)):
        line = lines[i].strip()
        if line:
            passport.line_into_fields(line)
        else:
            if passport.valid():
                valid += 1
            passport = Passport()
    print(valid)


if __name__ == '__main__':
    main()
