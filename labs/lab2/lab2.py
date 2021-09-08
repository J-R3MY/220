"""
Name: Jeremy Miller
lab2.py

Problem: This program performs arithmetic
"""
import math

def sum_of_threes():
    bound = eval(input("Enter a number: "))
    acc = 0
    for i in range(0, bound+1, 3):
        acc = acc+i

    print(acc)


def muliplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h*l, end=" ")
        print()

def triangle_area():
    a = eval(input("Input the length for side a: "))
    b = eval(input("Input the length for side b: "))
    c = eval(input("Input the length for side c: "))
    s = (a + b + c)/2
    A = (s*(s-a)*(s-b)*(s-c))
    Area = math.sqrt(A)
    print(Area)

def sumSquares():
    start = eval(input("Enter the start number: "))
    end = eval(input("Enter the ending number: "))
    acc = 0
    for i in range(start, end+1):
        acc = acc + i**2
    print(acc)


def power():
    base = eval(input("Enter a base number: "))
    exp = eval(input("Enter an exponent: "))
    acc = 1
    for i in range(exp):
        acc = acc * base

    print(base, "^", exp, "=", acc)

sum_of_threes()
muliplication_table()
triangle_area()
sumSquares()
power()
