import math


def get_value(grid, width, height, index, xoff, yoff):
    # index to coordinates
    x = index % width
    y = math.floor(index / width)
    # neighbor's coordinates
    nx = x + xoff
    ny = y + yoff
    while True:
        if not ((0 <= nx < width) and (0 <= ny < height)):
            return None
        else:
            nindex = ny * width + nx
            if grid[nindex] in ['L', '#']:
                return grid[nindex]
            else:
                nx += xoff
                ny += yoff


def count_adjacent(index, grid, width, height):
    adjacent = [
        get_value(grid, width, height, index, -1, -1),
        get_value(grid, width, height, index,  0, -1),
        get_value(grid, width, height, index,  1, -1),
        get_value(grid, width, height, index, -1,  0),
        get_value(grid, width, height, index,  1,  0),
        get_value(grid, width, height, index, -1,  1),
        get_value(grid, width, height, index,  0,  1),
        get_value(grid, width, height, index,  1,  1)
    ]
    return adjacent.count('#')


def step(grid, width, height):
    next = ''
    for index, cell in enumerate(grid):
        # Floor does nothing
        if cell == '.':
            next += '.'
            continue
        # Get counts
        occupied = count_adjacent(index, grid, width, height)
        # Seat stays the same or remains the same?
        if cell == 'L':
            if occupied == 0:
                next += '#'
            else:
                next += 'L'
        elif cell == '#':
            if occupied >= 5:
                next += 'L'
            else:
                next += '#'
        else:
            raise Exception(cell)
    return next


def display(grid, width):
    print('-' * width + '---')
    for i, cell in enumerate(grid):
        print(cell, end='')
        if (i+1) % width == 0:
            print()


def main():
    with open('input/11.data') as file:
        lines = file.read().splitlines()
    width = len(lines[0])
    height = len(lines)
    current = ''.join(lines).replace('L', '#')
    # display(current, width)  # DEBUG
    while True:
        next = step(current, width, height)
        if next == current:
            break
        current = next
        # display(current, width)  # DEBUG
    print('Occupied seats:', current.count('#'))


if __name__ == '__main__':
    main()
