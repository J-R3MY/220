"""
Name: Jeremy Miller
lab9.py
"""
import math

from graphics import Circle, GraphWin, Text, Point
from math import sqrt


def main():
    x = [1, 2, 3]
    addTen(x)
    print(x)
    y = [3, 5.7, 2]
    squareEach(y)
    print(y)
    z = [8, 5, 3]
    print(sumList(z))
    thisList = ["3", 5.7, "2"]
    print(toNumbers(thisList))
    writeSumofSquares()
    starter()
    leapYear(2100)
    circleOverlap()
    pass


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = nums[i] + acc
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])
    return strList


def writeSumofSquares():
    in_file = input('Enter the file name: ')
    in_file = open(in_file, 'r')
    out_file = open('output.txt', 'w')
    for line in in_file:
        split_line = line.split()
        toNumbers(split_line)
        squareEach(split_line)
        s = sumList(split_line)
        out_file.write('sum = ' + str(s) + "\n")


def starter():
    weight = eval(input('What is the weight?'))
    wins = eval(input('Number of wins: '))
    if weight >= 150 and weight < 160 and wins >= 5:
        print('The player should start')
    elif weight > 199 or wins > 20:
        print('The player should start')
    else:
        print('The player should not start')


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(str(year) + ' is a leap year')
    else:
        print(str(year) + ' is not a leap year')


def circleOverlap():
    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    circle1 = Circle(p1, radius1)
    circle1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    dist = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)

    pt = Point(200, 350)
    if dist < radius1 + radius2:
        text = Text(pt, 'The circles overlap.')
        text.draw(win)
    else:
        text = Text(pt, 'The circles do not overlap.')
        text.draw(win)
    win.getMouse()
    win.close()


main()
