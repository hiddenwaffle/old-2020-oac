import re

REGEX = re.compile(r'(\d+)-(\d+) ([a-z]): (.*)')  # https://pythex.org/


def parse_line(line):
    matches = REGEX.match(line)
    position1 = int(matches.group(1)) - 1
    position2 = int(matches.group(2)) - 1
    char = matches.group(3)
    password = matches.group(4)
    return position1, position2, char, password


def validate(line):
    position1, position2, char, password = parse_line(line)
    if password[position1] == char and password[position2] != char:
        return True
    if password[position1] != char and password[position2] == char:
        return True
    else:
        return False


def main():
    with open('input/02.data') as file:
        results = list(map(validate, file.read().splitlines()))
    print(sum(results))


if __name__ == '__main__':
    main()
