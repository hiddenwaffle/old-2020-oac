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


def main():
    with open('input/08.data') as file:
        ops = list(map(parse_op, file.read().splitlines()))
    acc = 0
    index = 0
    while True:
        acc, index, finished = step(ops, acc, index)
        if finished:
            break
    print(acc)


if __name__ == '__main__':
    main()
