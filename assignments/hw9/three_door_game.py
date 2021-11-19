"""
Name: Jeremy Miller
three_door_game.py

Problem: This program asks the user to guess the one correct door out of three doors

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from button import Button
from random import shuffle
from graphics import GraphWin, Point, Text


def main():
    win = GraphWin('Three Door Game', 600, 600)
    win.setCoords(0, 0, 600, 600)

    door_1 = Button(Point(125, 300), 70, 60, 'Door 1')
    door_1.draw(win)
    door_2 = Button(Point(300, 300), 70, 60, 'Door 2')
    door_2.draw(win)
    door_3 = Button(Point(475, 300), 70, 60, 'Door 3')
    door_3.draw(win)
    top_text = Text(Point(300, 500), 'I have a secret door')
    top_text.draw(win)
    bottom_text = Text(Point(300, 100), 'Click to choose my door')
    bottom_text.draw(win)
    mouse_click = win.getMouse()
    secret_list = [1, 2, 3]
    secret_value = 1
    shuffle(secret_list)
    door_1_value = secret_list[0]
    door_2_value = secret_list[1]
    door_3_value = secret_list[2]

    if door_1.is_clicked(mouse_click) and door_1_value == secret_value:
        door_1.color_button('green')
        top_text.setText('You Win!')
        bottom_text.setText('Click to close')
    elif door_1.is_clicked(mouse_click) and door_1_value != secret_value:
        door_1.color_button('red')
        top_text.setText('You Lost!')
        if door_2_value == secret_value:
            bottom_text.setText('Door 2 is my secret door')
        elif door_3_value == secret_value:
            bottom_text.setText('Door 3 is my secret door')
    elif door_2.is_clicked(mouse_click) and door_2_value == secret_value:
        door_2.color_button('green')
        top_text.setText('You Win!')
        bottom_text.setText('Click to close')
    elif door_2.is_clicked(mouse_click) and door_2_value != secret_value:
        door_2.color_button('red')
        top_text.setText('You Lost!')
        if door_1_value == secret_value:
            bottom_text.setText('Door 1 is my secret door')
        elif door_3_value == secret_value:
            bottom_text.setText('Door 3 is my secret door')
    elif door_3.is_clicked(mouse_click) and door_3_value == secret_value:
        door_3.color_button('green')
        top_text.setText('You Win!')
        bottom_text.setText('Click to close')
    elif door_3.is_clicked(mouse_click) and door_3_value != secret_value:
        door_3.color_button('red')
        top_text.setText('You Lost!')
        if door_2_value == secret_value:
            bottom_text.setText('Door 2 is my secret door')
        elif door_1_value == secret_value:
            bottom_text.setText('Door 1 is my secret door')

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
