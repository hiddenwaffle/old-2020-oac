import copy


def add_rule(line, rules):
    parts = line.split(' contain ')
    lhs = parts[0]
    rhs = parts[1].replace('.', '').split(', ')
    rules[lhs] = []
    for child in rhs:
        if child == 'no other bag':
            pass  # Lowest level
        else:
            qty, next_bag = child.split(' ', 1)
            rules[lhs].append((int(qty), next_bag))


def find_path(rules, prev_path, start, target):
    path = copy.copy(prev_path)
    path.append(start)
    if start == target:
        return path  # Found
    for rule in rules[start]:
        max_bags, next_bag = rule
        result = find_path(rules, path, next_bag, target)
        if result:
            return result
    return None


def find_parents(rules, target):
    parents = []
    for start in rules:
        if start == target:
            pass
        else:
            found_path = find_path(rules, [], start, target)
            if found_path:
                parents.append(start)
    return parents


def count_nested_bags(rules, start_bag):
    count = 0
    for rule in rules[start_bag]:
        print(start_bag, '->', rule)
        num_bags, next_bag = rule
        for _ in range(num_bags):
            count += 1 + count_nested_bags(rules, next_bag)
    return count


def main():
    with open('input/07.data') as file:
        lines = file.read().replace('bags', 'bag').splitlines()
    rules = {}
    for line in lines:
        add_rule(line, rules)
    # parents = find_parents(rules, 'shiny gold bag')
    # print(len(parents), parents)
    count = count_nested_bags(rules, 'shiny gold bag')
    print(count)


if __name__ == '__main__':
    main()
