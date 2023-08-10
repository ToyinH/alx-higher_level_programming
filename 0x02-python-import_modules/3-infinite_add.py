#!/usr/bin/python3
def main():
    from sys import argv
    elements = len(argv)
    if elements == 1:
        print("0")
    else:
        sum = 0
        for element in range(elements):
            if element > 0:
                sum += int(argv[element])
        print(sum)


if __name__ == "__main__":
    main()
