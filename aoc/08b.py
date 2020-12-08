import copy


def is_positive(char):
    if char == '+':
        return True
    elif char == '-':
        return False
    raise Exception(char)


def parse_op(line):
    command, arg = line.split(' ')
    positive = is_positive(arg[0])
    offset = int(arg[1:])
    return [command, positive, offset, False]  # False means has not yet executed


def step(ops, acc, index):
    command, positive, offset, executed = ops[index]
    if executed:
        return acc, index, True
    else:
        ops[index][3] = True
        if command == 'nop':
            return acc, index + 1, False
        elif command == 'jmp':
            if positive:
                return acc, index + offset, False
            else:
                return acc, index - offset, False
        elif command == 'acc':
            if positive:
                return acc + offset, index + 1, False
            else:
                return acc - offset, index + 1, False
        else:
            raise Exception(command)


def try_flip(ops, index):
    op = ops[index]
    print('Checking flip on:', op)
    if op[0] == 'nop':
        op[0] = 'jmp'
    elif op[0] == 'jmp':
        op[0] = 'nop'
    acc = 0
    index = 0
    while index < len(ops):
        acc, index, finished_too_soon = step(ops, acc, index)
        if finished_too_soon:
            return False, acc
    return True, acc


def main():
    with open('input/08.data') as file:
        original_ops = list(map(parse_op, file.read().splitlines()))
    for index in range(len(original_ops)):
        ops = copy.deepcopy(original_ops)
        success, acc = try_flip(ops, index)
        if success:
            print(acc, '<--- for index:', index)
            break
        else:
            print('Failed index:', index)


if __name__ == '__main__':
    main()
