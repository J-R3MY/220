"""
Name: Jeremy Miller
vigenere.py

Problem: This program uses a vigenere cipher to encrypt a message

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import GraphWin, Text, Rectangle, Entry, Point


def main():
    win = GraphWin('Vigenere', 500, 500)
    win.setCoords(0, 0, 10, 10)

    message_input = Entry(Point(6, 8), 30)
    key_input = Entry(Point(4.6, 7), 15)
    message_input.draw(win)
    key_input.draw(win)

    message_text = Text(Point(1.7, 8), 'Message to Code:')
    key_text = Text(Point(2, 7), 'Enter keyword:')
    message_text.draw(win)
    key_text.draw(win)

    button_outline = Rectangle(Point(4, 6.5), Point(6, 5.5))
    center = button_outline.getCenter()
    button_text = Text(center, 'Encode')
    button_text.draw(win)
    button_outline.draw(win)

    win.getMouse()

    button_text.undraw()
    button_outline.undraw()

    message = message_input.getText()
    key = key_input.getText()

    encode_message = Text(Point(5, 5), 'Resulting Message:')
    encode_message.draw(win)
    close_message = Text(Point(5, 0.5), 'Click Anywhere to Close Window')
    close_message.draw(win)

    output_text = Text(Point(5, 4), '')
    output_text.setText(code(message, key))
    output_text.draw(win)

    win.getMouse()
    win.close()


def code(message, key):
    message = message.upper().replace(' ', '')
    key = key.upper().replace(' ', '')
    cipher_text = ''
    for i in range(len(message)):
        character = ord(message[i]) - 65
        new_key = ord(key[i % len(key)]) - 65
        shift = (character + new_key) % 26 + 65
        cipher_text = cipher_text + chr(shift)
    return cipher_text


if __name__ == '__main__':
    main()

