#!/usr/bin/python3
def main():
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if not name[0:2] == "__":
            print(name)


if __name__ == "__main__":
    main()

