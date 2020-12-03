def main():
    with open('input/01.data') as file:
        numbers = list(map(int, file.read().splitlines()))
    results = [x * y
               for x in numbers
               for y in numbers
               if x != y and x + y == 2020]
    print(results)


if __name__ == '__main__':
    main()
