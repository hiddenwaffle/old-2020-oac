def combine(register):
    return len(set.intersection(*register))


def main():
    with open('input/06.data') as file:
        lines = file.read().splitlines()
    lines.append('')  # Prevent off-by-1
    total = 0
    register = []
    for line in lines:
        if line:
            questions = set()
            register.append(questions)
            for yes in line:
                questions.add(yes)
        else:
            total += combine(register)
            register = []
    print(total)


if __name__ == '__main__':
    main()
