from math import inf


def to_int(x):
    if x.isnumeric():
        return int(x)
    else:
        return None


def main():
    with open('input/13.data') as file:
        lines = file.read().splitlines()
    start_time = int(lines[0])
    buses = [bus for bus in list(map(to_int, lines[1].split(',')))
             if bus]  # Filter out None elements
    nearest_bus = None
    nearest_diff = inf
    for bus in buses:
        x = start_time // bus
        y = bus * (x + 1)
        diff = y - start_time
        if diff < nearest_diff:
            nearest_bus = bus
            nearest_diff = diff
    print(nearest_bus * nearest_diff)


def thing():
    print('doing the thing')
    return 10


if __name__ == '__main__':
    main()
