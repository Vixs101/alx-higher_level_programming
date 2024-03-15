#!/usr/bin/python3
from sys import argv


def main():
    total = 0

    if len(argv) == 1:
        print("{}".format(total))
    elif len(argv) > 1:
        start_index = 1
        for i in range(start_index, len(argv)):
            total = total + int(argv[i])
        print("{}".format(total))


if __name__ == "__main__":
    main()
