#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper = "".join(chr(ord(char) - 32))
        else:
            upper = "".join(char)
        print("{:s}".format(upper), end="")
    print()
