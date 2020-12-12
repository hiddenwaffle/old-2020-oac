import math


def to_action(line):
    return line[0], int(line[1:])


def rotate(given_amount, x, y):
    nx = x * math.cos(math.radians(given_amount)) - y * math.sin(math.radians(given_amount))
    ny = x * math.sin(math.radians(given_amount)) + y * math.cos(math.radians(given_amount))
    return round(nx), round(ny)


def main():
    with open('input/12.data') as file:
        actions = list(map(to_action, file.read().splitlines()))
    ship_x = 0
    ship_y = 0
    wp_x = 10
    wp_y = 1
    for type, amount in actions:
        if type == 'N':
            wp_y += amount
        elif type == 'S':
            wp_y -= amount
        elif type == 'E':
            wp_x += amount
        elif type == 'W':
            wp_x -= amount
        elif type == 'L':
            wp_x, wp_y = rotate(amount, wp_x, wp_y)
        elif type == 'R':
            wp_x, wp_y = rotate(-amount, wp_x, wp_y)
        elif type == 'F':
            ship_x += wp_x * amount
            ship_y += wp_y * amount
        else:
            raise Exception(type)
        print(type, amount, '-> ship:', ship_x, ship_y, '-- wp:', wp_x, wp_y)
    print('Absolute values of', ship_x, 'and', ship_y, 'sum to', abs(ship_x) + abs(ship_y))


if __name__ == '__main__':
    main()
