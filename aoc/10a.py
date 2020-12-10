def main():
    with open('input/10.data') as file:
        ratings = sorted(list(map(int, file.read().splitlines())))
    diff1 = 0
    diff2 = 0
    diff3 = 0
    current = 0
    for rating in ratings:
        diff = rating - current
        if diff == 1:
            diff1 += 1
        elif diff == 2:
            diff2 += 1
        elif diff == 3:
            diff3 += 1
        else:
            raise Exception(diff)
        current = rating
    diff3 += 1  # The device
    print(diff1, diff2, diff3)
    print(diff1 * diff3)


if __name__ == '__main__':
    main()
