import sys


def get_numbers():
    if len(sys.argv) == 3:
        result = []
        index = 1
        while index < 3:
            result.append(int(sys.argv[index]))
            index += 1
        return result
    else:
        print("WARNING: Provide two numbers, by calling: python sum.py x y.")
        return -1


def main():
    numbers = get_numbers()
    suma = sum(numbers)
    print(suma)


if __name__ == "__main__":
    main()