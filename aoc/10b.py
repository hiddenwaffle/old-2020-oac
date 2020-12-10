def count_next(rating, ratings):
    index = ratings.index(rating)
    candidates = []
    for other in ratings[index + 1:index + 4]:
        if other <= rating + 3:
            candidates.append(other)
    return candidates


def do_it(register):
    for key in register:
        nexts = register[key]
        if len(nexts) < 1:
            register[key] = 1
        else:
            acc = 0
            for next in nexts:
                acc += register[next]
            register[key] = acc
    print(register[0])


def main():
    with open('input/10.data') as file:
        ratings = sorted(list(map(int, file.read().splitlines())))
    ratings.insert(0, 0)  # outlet
    ratings.append(ratings[-1] + 3)  # device
    register = {}
    for rating in reversed(ratings):
        register[rating] = count_next(rating, ratings)
    do_it(register)


if __name__ == '__main__':
    main()
