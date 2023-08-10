#!/usr/bin/python3
def main():
    from sys import argv, exit
    elements = len(argv)
    if elements == 1:
        argument = elements - 1
        print("{} arguments.".format(argument))
    elif elements == 2:
        argument = elements - 1
        print("{} argument:".format(argument))
        for elements in range(len(argv)):
            if elements > 0:
                print("{}: {}".format(elements, argv[elements]))
    else:
        argument = elements - 1
        print("{} arguments:".format(argument))
        for elements in range(len(argv)):
            if elements > 0:
                print("{}: {}".format(elements, argv[elements]))


if __name__ == "__main__":
    main()
