def main():
    with open('input/03.data') as file:
        lines = file.read().splitlines()
    num_cols = len(lines[0])
    num_rows = len(lines)
    col = 0
    row = 0
    tree_count = 0
    while row < num_rows:
        if lines[row][col] == '#':
            tree_count += 1
        # Next step
        col = (col + 3) % num_cols
        row = row + 1
    print(tree_count)


if __name__ == '__main__':
    main()
