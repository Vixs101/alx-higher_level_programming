#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for index, value in enumerate(argv[1:], start=1):
            print("{}: {}".format(index, value))


if __name__ == "__main__":
    main()
