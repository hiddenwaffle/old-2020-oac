def ensure_pair(candidates, target):
    candidate_pairs = [(a, b) for a in candidates for b in candidates if a != b]
    for a, b in candidate_pairs:
        if a + b == target:
            # print(a, b, target)
            return True
    else:
        return False


def main():
    with open('input/09.data') as file:
        numbers = list(map(int, file.read().splitlines()))
    preamble = 25
    for i in range(preamble, len(numbers)):
        candidates = numbers[i-preamble:i]
        target = numbers[i]
        if not ensure_pair(candidates, target):
            print(candidates, target)
            break
    else:
        raise Exception('Should not get here')


if __name__ == '__main__':
    main()
