def adjust_range(low, high, half):
    mid_start = (low + high + 1) / 2
    if half == 'lower':
        return low, mid_start - 1
    elif half == 'upper':
        return mid_start, high
    else:
        raise Exception(half)


def bsp_to_seat(line):
    row_low = 0
    row_high = 127
    for fb in line[:7]:
        if fb == 'F':
            row_low, row_high = adjust_range(row_low, row_high, 'lower')
        elif fb == 'B':
            row_low, row_high = adjust_range(row_low, row_high, 'upper')
        else:
            raise Exception(fb)
    if row_low != row_high:
        raise Exception(f'{row_low}, {row_high}')
    seat_low = 0
    seat_high = 7
    for lr in line[7:10]:
        if lr == 'L':
            seat_low, seat_high = adjust_range(seat_low, seat_high, 'lower')
        elif lr == 'R':
            seat_low, seat_high = adjust_range(seat_low, seat_high, 'upper')
        else:
            raise Exception(lr)
    if seat_low != seat_high:
        raise Exception(f'{seat_low}, {seat_high}')
    return row_low * 8 + seat_low


def main():
    with open('input/05.data') as file:
        lines = file.read().splitlines()
    seats = []
    for line in lines:
        seat = bsp_to_seat(line)
        seats.append(seat)
    seats = sorted(map(int, seats))
    for i in range(63, 935 + 1):
        if i not in seats:
            print(i)


if __name__ == '__main__':
    main()
