def ensure_pair(candidates, target):
    candidate_pairs = [(a, b) for a in candidates for b in candidates if a != b]
    for a, b in candidate_pairs:
        if a + b == target:
            # print(a, b, target)
            return True
    else:
        return False


def find_contiguous(candidates, target):
    bound_pairs = [(a, b) for a in range(1000) for b in range(1000) if a < b]
    for a, b in bound_pairs:
        values = candidates[a:b]
        if sum(values) == target:
            return values
    raise Exception(candidates, target)


def main():
    with open('input/09.data') as file:
        numbers = list(map(int, file.read().splitlines()))
    preamble = 25
    for i in range(preamble, len(numbers)):
        candidates = numbers[i - preamble:i]
        target = numbers[i]
        if not ensure_pair(candidates, target):
            # print(candidates, target)
            result = target
            result_i = i
            break
    else:
        raise Exception('Should not get here')
    final_candidates = numbers[:result_i]  # Won't be higher than the rest
    weakness_terms = sorted(find_contiguous(final_candidates, result))
    print('weakness', weakness_terms[0] + weakness_terms[-1])


if __name__ == '__main__':
    main()
