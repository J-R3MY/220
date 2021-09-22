"""
Name: Jeremy Miller
lab4.py
"""
from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    inst_pt = Point(width / 2, height - 390)
    instructions = Text(inst_pt, "Click 2 points to make a rectangle")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    rec = Rectangle(p1, p2)
    rec.setFill("blue")
    rec.draw(win)
    r_length = abs(p1.getX() - p2.getX())
    r_width = abs(p1.getY() - p2.getY())
    area = r_length * r_width
    perimeter = 2 * (r_length + r_width)

    inst_pt1 = Point(width / 2, height - 10)
    area_text = Text(inst_pt1, "The area is: " + str(area))
    area_text.draw(win)
    inst_pt2 = Point(width / 2, height - 25)
    perimeter_text = Text(inst_pt2, "The perimeter is: " + str(perimeter))
    perimeter_text.draw(win)

    instructions.undraw()
    inst_pt = Point(width / 2, height - 390)
    instructions = Text(inst_pt, "Click to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Make a circle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click two points to make a circle")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
    r = math.sqrt(d)
    c = Circle(p1, r)
    c.setFill("orange")
    c.draw(win)

    inst_pt2 = Point(width / 2, height - 25)
    radius_text = Text(inst_pt2, "The radius is: " + str(r))
    radius_text.draw(win)
    instructions.undraw()
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def pi2():
    num = eval(input("How many times do you want to run: "))
    acc = 0
    for i in range(num):
        num = 4
        denom = 1+2*i
        frac = (num / denom) * ((-1)**i)
        acc = acc + frac
    print(math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
