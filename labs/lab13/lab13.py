"""
Name: Jeremy Miller
lab13.py
"""
from graphics import *


def main():
    x = [3, 4, 1, 6]
    is_in_binary(3, [1, 2, 3])
    selection_sort(x)
    print(x)
    trade_alert('trades.txt')
    pass


def is_in_binary(search_val, values):
    left = 0
    right = len(values)-1
    while left <= right:
        mid = (left + right) // 2
        mid_value = values[mid]
        if search_val == mid_value:
            return mid
        if search_val < mid_value:
            right = mid - 1
        if search_val > mid_value:
            left = mid + 1
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def rect_sort(rectangles):
    dict = {}
    areas = []
    for rect in rectangles:
        dict[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dict[areas[i]]


def trade_alert(filename):
    in_file = open(filename, 'r')
    data = in_file.read().split()
    i = 0
    while i < len(data):
        pos = i + 1
        if int(data[i]) > 830:
            print('ALERT! Trading volume exceeds 830 at', pos, 'seconds!')
        if int(data[i]) == 500 and int(data[i]) < 830:
            print('WARNING! Trading volume is equal to 500 at', pos, 'seconds!')
        i += 1


def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    w = abs(p1.getX() - p2.getY())
    h = abs(p1.getY() - p2.getY())
    return w * h


main()
