def main():
    with open('input/01.data') as file:
        numbers = list(map(int, file.read().splitlines()))
    results = [x * y * z
               for x in numbers
               for y in numbers
               for z in numbers
               if x != y and x != z and y != z and x + y + z == 2020]
    print(results)


if __name__ == '__main__':
    main()
