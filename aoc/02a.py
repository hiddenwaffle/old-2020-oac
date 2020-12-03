import re

REGEX = re.compile(r'(\d+)-(\d+) ([a-z]): (.*)')  # https://pythex.org/


def parse_line(line):
    matches = REGEX.match(line)
    lower_bound = int(matches.group(1))
    upper_bound = int(matches.group(2))
    char = matches.group(3)
    password = matches.group(4)
    return lower_bound, upper_bound, char, password


def validate(line):
    lower_bound, upper_bound, char, password = parse_line(line)
    return lower_bound <= password.count(char) <= upper_bound


def main():
    with open('input/02.data') as file:
        results = list(map(validate, file.read().splitlines()))
    print(sum(results))


if __name__ == '__main__':
    main()
