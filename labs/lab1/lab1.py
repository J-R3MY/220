"""
Name: <Jeremy Miller>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    total_shots = eval(input("How many total shots did you make?: "))
    shots_made = eval(input("How many shots did you successfully make?: "))
    percentage = shots_made / total_shots * 100
    print("Percentage Made:", percentage)

def coffee():
    coffee_pounds = eval(input("How many pounds of coffee did you purchase?: "))
    price_per_pound = 10.50
    shipping = .86
    fixed_cost = 1.50
    total = price_per_pound * coffee_pounds + shipping * coffee_pounds + fixed_cost
    print("Total:", total)

def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?: "))
    miles = kilometers / 1.61
    print("You traveled", miles, "miles")

#calc_rec_area()
#calc_volume()
#shooting_percentage()
#coffee()
kilometers_to_miles()