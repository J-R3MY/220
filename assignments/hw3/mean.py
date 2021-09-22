"""
Name: Jeremy Miller
mean.py

Problem: This program uses three different methods for calculating a mean of a set of numbers

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
import math


def main():
    num = eval(input("Enter the values to be entered: "))
    acc0 = 0
    acc1 = 0
    acc2 = 1
    for i in range(num):
        values = eval(input("Enter value " + str(i+1) + ": "))
        acc0 = acc0 + values ** 2
        acc1 = acc1 + (1/values)
        acc2 = acc2 * values

    rms_avg = math.sqrt(acc0/num)
    print(round(rms_avg, 3))
    harmonic_mean = num / acc1
    print(round(harmonic_mean, 3))
    geometric_mean = acc2**(1/num)
    print(round(geometric_mean, 3))


if __name__ == '__main__':
    main()
