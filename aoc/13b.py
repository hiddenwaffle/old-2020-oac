from math import inf


def to_int(x):
    if x.isnumeric():
        return int(x)
    else:
        return None


def main():
    with open('input/13_example.data') as file:
        lines = file.read().splitlines()
    buses = list(map(to_int, lines[1].split(',')))
    print(buses)


def thing():
    print('doing the thing')
    return 10


if __name__ == '__main__':
    main()
