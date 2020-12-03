def slide(right, down, lines):
    num_cols = len(lines[0])
    num_rows = len(lines)
    col = 0
    row = 0
    tree_count = 0
    while row < num_rows:
        if lines[row][col] == '#':
            tree_count += 1
        # Next step
        col = (col + right) % num_cols
        row = row + down
    return tree_count


def main():
    with open('input/03.data') as file:
        lines = file.read().splitlines()
    _1_1 = slide(1, 1, lines)
    _3_1 = slide(3, 1, lines)
    _5_1 = slide(5, 1, lines)
    _7_1 = slide(7, 1, lines)
    _1_2 = slide(1, 2, lines)
    print(_1_1 * _3_1 * _5_1 * _7_1 * _1_2)


if __name__ == '__main__':
    main()
