def main():
    with open('input/08_example.data') as file:
        lines = file.read().replace('bags', 'bag').splitlines()
    print(lines)


if __name__ == '__main__':
    main()
