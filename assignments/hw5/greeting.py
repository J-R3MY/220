"""
Name: Jeremy Miller
greeting.py

Problem: This program draws a valentines card

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from time import sleep
from graphics import GraphWin, Point, Polygon, Text, Line


def main():
    width = 450
    height = 600
    win = GraphWin("Valentine Card", width, height)
    win.setCoords(0, 0, 15, 20)
    happy_text = Text(Point(7.5, 3), "HAPPY VALENTINE'S DAY!")
    happy_text.draw(win)
    win.setBackground("pink")

    shape = Polygon(Point(2, 11), Point(2, 14), Point(3.5, 16), Point(6, 16), Point(7.5, 14.5),
                    Point(9, 16), Point(11.5, 16), Point(13, 14), Point(13, 11), Point(7.5, 5))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    shoot_text = Text(Point(7.5, 12), 'Click to Shoot the Heart')
    shoot_text.setFill('white')
    shoot_text.draw(win)
    win.getMouse()

    point_1 = Point(0, 0)
    point_2 = Point(2.5, 3)

    line = Line(point_1, point_2)
    line.setArrow("last")
    line.setWidth(2)
    line.draw(win)

    for _ in range(15):
        line.move(1, 1.25)
        sleep(0.1)

    happy_text.undraw()
    close_text = Text(Point(7.5, 3), 'Click Anywhere to Close')
    close_text.draw(win)

    win.getMouse()
    win.close()


main()
