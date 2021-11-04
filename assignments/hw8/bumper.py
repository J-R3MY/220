"""
Name: Jeremy Miller
bumper.py

Problem: This program makes balls bounce around in a window

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from time import sleep
from random import randint, randrange
from math import sqrt
from graphics import GraphWin, Circle, Point, color_rgb


def main():
    win_width = 300
    win_height = 300
    win = GraphWin('Bumper', win_width, win_height)
    win.setCoords(0, 0, win_width, win_height)
    win.setBackground('black')
    radius = 20

    win_width_left = radius  # center is separated from the wall by the radius at a collision
    win_width_right = win_width - radius
    win_height_bottom = radius
    win_height_top = win_height - radius

    center1 = get_random_point(win_width_left, win_width_right,
                               win_height_bottom, win_height_top)
    center2 = get_random_point(win_width_left, win_width_right,
                               win_height_bottom, win_height_top)

    circle1 = make_circle(center1, radius, win)
    circle2 = make_circle(center2, radius, win)

    move_in_win(circle1, circle2, win)

    win.close()


def move_in_win(shape1, shape2, win):
    dx_1 = get_random(3)
    dy_1 = get_random(5)
    dx_2 = get_random(4)
    dy_2 = get_random(6)
    while 1 > 0:
        shape1.move(dx_1, dy_1)
        shape2.move(dx_2, dy_2)
        if hit_horizontal(shape1, win):
            dy_1 = -dy_1
            # print('Ball 1 Hit Horizontal Wall')
        if hit_horizontal(shape2, win):
            dy_2 = -dy_2
            # print('Ball 2 Hit Horizontal Wall')
        if hit_vertical(shape1, win):
            dx_1 = -dx_1
            # print('Ball 1 Hit Vertical Wall')
        if hit_vertical(shape2, win):
            dx_2 = -dx_2
            # print('Ball 2 Hit Vertical Wall')
        if did_collide(shape1, shape2):
            dx_1 = -dx_1
            dy_1 = -dy_1
            dx_2 = -dx_2
            dy_2 = -dy_2
            # print('The Balls Collided!!')
            # print(did_collide(shape1, shape2))
        sleep(.01)


def hit_horizontal(circle, win):
    center = circle.getCenter()
    y_coord = center.getY()
    radius = circle.getRadius()
    win_height_bottom = radius
    win_height_top = win.getHeight() - radius
    return y_coord <= win_height_bottom or y_coord >= win_height_top


def hit_vertical(circle, win):
    center = circle.getCenter()
    x_coord = center.getX()
    radius = circle.getRadius()
    win_width_left = radius
    win_width_right = win.getWidth() - radius
    # print('X:', x_coord <= win_width_left or x_coord >= win_width_right)
    return x_coord <= win_width_left or x_coord >= win_width_right


def did_collide(circle1, circle2):
    center1 = circle1.getCenter()
    center2 = circle2.getCenter()
    radius = circle1.getRadius()
    x_1 = center1.getX()
    y_1 = center1.getY()
    x_2 = center2.getX()
    y_2 = center2.getY()
    dist = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return dist < radius


def make_circle(center, radius, win):
    circle = Circle(center, radius)
    color = get_random_color()
    circle.setOutline(color)
    circle.setFill(color)
    circle.draw(win)
    return circle


def get_random_color():
    red = randint(0, 256)
    green = randint(0, 256)
    blue = randint(0, 256)
    return color_rgb(red, green, blue)


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def get_random_point(x_left, x_right, y_bottom, y_top):
    x_coord = randrange(x_left, x_right + 1)
    y_coord = randrange(y_bottom, y_top + 1)
    return Point(x_coord, y_coord)


if __name__ == '__main__':
    main()
