#!/usr/bin/python3

for tens_digit in range(0, 10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit != 8 or ones_digit != 9:
            print("{:d}{:d}, ".format(tens_digit, ones_digit), end="")

print("89")
