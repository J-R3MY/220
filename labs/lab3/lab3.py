"""
Name: Jeremy Miller
lab3.py

Problem: This program performs arithmetic using loops
"""

def average():
    num = eval(input("Enter the number of homework assignments: "))
    acc = 0
    for i in range(num):
        hw = eval(input("Enter your grade on HW" + str(i+1) + ": "))
        acc = acc + hw

    avg = acc / num
    print("The average is:", avg)


def tip_jar():
    acc = 0
    for i in range(5):
        donation = eval(input("Enter the amount of your donation: "))
        acc = acc + donation
    print("The donation total is:", acc)


def newton():
    root = eval(input("Enter the number you want to approximate the root of: "))
    refine = eval(input("How many times do you want to refine the approximation: "))
    approx = root / 2
    for i in range(refine):
        approx = ((approx + (root / approx)) / 2)

    print(approx)



def sequence():
    x = eval(input("Enter the number of terms in a series: "))
    for i in range(1, x + 1):
        y = 1 + (i//2 * 2)
        print(y, end=" ")

    print()


def pi():
    n = eval(input("How many terms in the sequence: "))
    acc = 1
    for i in range(n):
        num = 2 + (i//2 * 2)
        denom = 1 + ((i+1)//2 * 2)
        frac = num / denom
        acc = frac * acc

    print(acc * 2)


average()
tip_jar()
newton()
sequence()
pi()
