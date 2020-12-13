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
    # The earliest timestamp that matches the list 17,x,13,19 is 3417.
    #
    # 17 - (t % 17) = 17
    # 13 - (t % 13) = 2
    # 19 - (t % 19) = 3
    #
    # t % 17 = 0
    # t % 13 = 11
    # t % 19 = 16
    #
    # TODO: Use the Extended Euclidean algorithm to find t?


if __name__ == '__main__':
    main()
