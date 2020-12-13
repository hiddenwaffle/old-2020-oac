def to_int(x):
    if x.isnumeric():
        return int(x)
    else:
        return None


def main():
    with open('input/13.data') as file:
        lines = file.read().splitlines()
    buses = list(map(to_int, lines[1].split(',')))
    equations = []
    for i, bus in enumerate(buses):
        if bus:
            equations.append(f'mod[t, {bus}] = {i}')
    print(', '.join(equations))  # Paste into Wolfram Alpha
    t = buses[0]
    pindex = 0
    remainders = [0] * len(buses)
    for i, bus in enumerate(buses):
        if bus:
            remainders[i] = (bus - i) % buses[i]
        else:
            remainders[i] = None
    while True:
        success = True
        for i, bus in enumerate(buses):
            if bus:
                if t % bus != remainders[i]:
                    success = False
                    break
                else:
                    pass
        if success:
            print('Success:', t)
            break
        t += buses[0]
        pindex += 1
        if pindex % 90000000 == 0:
            print('t', t)
            pindex = 0

    # OLD NOTES:
    # The earliest timestamp that matches the list 17,x,13,19 is 3417.
    #
    # 17 - (t % 17) = 17    <-- since 17 % itself is 0
    # 13 - (t % 13) = 2     <-- where 2 is offset+2
    # 19 - (t % 19) = 3     <-- where 3 is offset+3
    #
    # t % 17 = 0
    # t % 13 = 11
    # t % 19 = 16
    #
    # TODO: Use the Extended Euclidean algorithm to find t?


if __name__ == '__main__':
    main()
