#!/usr/bin/python3
for tens in range(10):
    for ones in range(10):
        if tens < ones and not (tens == 8 and ones == 9):
            print("{:d}{:d}".format(tens, ones), end=", ")
        if tens == 8 and ones == 9:
            print("{:d}{:d}".format(tens, ones))
