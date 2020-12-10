def count_next(ratings):
    print(ratings)
    if not ratings:
        return 1
    current = ratings[0]
    candidates = []
    for candidate_i in range(1, 4):
        if candidate_i >= len(ratings):
            break
        candidate = ratings[candidate_i]
        if candidate <= current+3:
            candidates.append((candidate, candidate_i))
    if not candidates:
        return 1
    else:
        acc = len(candidates)
        for candidate, candidate_i in candidates:
            print('going from', current, 'to', candidate, 'out of', len(candidates))
            acc *= count_next(ratings[candidate_i:])
        return acc


def main():
    with open('input/10_example.data') as file:
        ratings = sorted(list(map(int, file.read().splitlines())))
    ratings.insert(0, 0)  # outlet
    ratings.append(ratings[-1]+3)  # device
    result = count_next(ratings)
    print('distinct ways to arrange the adapters:', result)


if __name__ == '__main__':
    main()
