from itertools import chain, combinations


# https://stackoverflow.com/a/1482316
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def ensure_pair(candidates, target):
    candidate_pairs = [(a, b) for a in candidates for b in candidates if a != b]
    for a, b in candidate_pairs:
        if a + b == target:
            # print(a, b, target)
            return True
    else:
        return False


# https://stackoverflow.com/a/28885643
def is_sequential(mylist):
    for i in range(len(mylist)-1):
        if mylist[i]+1 != mylist[i+1]:
            return False
    return True


def find_contiguous(candidates, target):
    summers = [x for x in list(powerset(candidates)) if sum(x) == target]
    for summer in summers:
        indices = list(map(lambda a: candidates.index(a), summer))
        if is_sequential(indices):
            print('summer:', summer)
            return summer
    raise Exception(candidates, target)


def main():
    with open('input/09_example.data') as file:
        numbers = list(map(int, file.read().splitlines()))
    preamble = 5
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
