#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
str1 = "Last digit of"
str2 = "and is less than 6 and not 0"
if num > 5 and number > 0:
    print("{:s} {:d} is {:d} and is greater than 5".format(str1, number, num))
elif num == 0:
    print("{:s} {:d} is {:d} and is 0".format(str1, number, num))
elif num < 6 and num != 0:
    if number < 0:
        print("{:s} {:d} is -{:d} {:s}".format(str1, number, num, str2))
    else:
        print("{:s} {:d} is {:d} {:s}".format(str1, number, num, str2))
