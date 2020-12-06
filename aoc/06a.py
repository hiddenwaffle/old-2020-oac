def main():
    with open('input/06.data') as file:
        lines = file.read().splitlines()
    lines.append('')  # Prevent off-by-1
    total = 0
    questions = set()
    for line in lines:
        if not line:
            total += len(questions)
            questions = set()
        else:
            for yes in line:
                questions.add(yes)
    print(total)


if __name__ == '__main__':
    main()
