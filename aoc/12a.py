def to_action(line):
    return line[0], int(line[1:])


def main():
    with open('input/12.data') as file:
        actions = list(map(to_action, file.read().splitlines()))
    ship_facing = 0
    ship_x = 0
    ship_y = 0
    for type, amount in actions:
        if type == 'N':
            ship_y += amount
        elif type == 'S':
            ship_y -= amount
        elif type == 'E':
            ship_x += amount
        elif type == 'W':
            ship_x -= amount
        elif type == 'L':
            ship_facing = (ship_facing + amount) % 360
        elif type == 'R':
            ship_facing = (ship_facing - amount) % 360
        elif type == 'F':
            if ship_facing == 0:
                ship_x += amount
            elif ship_facing == 90:
                ship_y += amount
            elif ship_facing == 180:
                ship_x -= amount
            elif ship_facing == 270:
                ship_y -= amount
            else:
                raise Exception(ship_facing)
        else:
            raise Exception(type)
        print(type, amount, '->', ship_x, ship_y, ship_facing)
    print('Absolute values of', ship_x, 'and', ship_y, 'sum to', abs(ship_x) + abs(ship_y))


if __name__ == '__main__':
    main()
