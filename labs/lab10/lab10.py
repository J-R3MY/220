"""
Name: Jeremy Miller
lab10.py
"""


def main():
    play_game()
    pass


def build_board():
    return list(range(1,10))


def display_board(board):
    for i in range(3):
        n = i*3
        print(board[n], board[n+1], board[n+2], sep=' | ')
        print(9 * "-")


def place(board, pos, piece):
    if piece in ('X', 'O'):
        board[pos-1] = piece


def legal(board, pos):
    if (pos >= 1 and pos <= 9) and (board[pos-1] != 'X' and board[pos-1] != 'Y'):
        return True
    return False


def game_won(board, piece):
    # horizontal
    for i in range(3):
        n = i*3
        if board[n] != piece:
            continue
        if board[n+1] != piece:
            continue
        if board[n+2] != piece:
            continue
        return True
    # vertical
    for i in range(3):
        if board[i] != piece:
            continue
        if board[i+3] != piece:
            continue
        if board[i+6] != piece:
            continue
        return True
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    return False


def game_over(board):
    if game_won(board, 'X'):
        return True
    elif game_won(board, 'O'):
        return True
    else:
        for i in range(9):
            if board[i] == i+1:
                return False
        return True


def play_game():
    board = build_board()
    while True:
        display_board(board)
        # let x play
        x_pos = eval(input('Where do you want to put X? '))
        while not legal(board, x_pos):
            x_pos = eval(input('Not a legal move! Try again! '))
        place(board, x_pos, 'X')
        if game_over(board):
            if game_won(board, 'X'):
                display_board(board)
                print('X wins!')
                exit()
            elif game_won(board, 'O'):
                display_board(board)
                print('O wins!')
                exit()
            else:
                display_board(board)
                print('Tie!')
                exit()
        display_board(board)
        # let y play
        o_pos = eval(input('Where do you want to put O?' ))
        while not legal(board, o_pos):
            o_pos = eval(input('Not a legal move! Try again!' ))
        place(board, o_pos, 'O')
        if game_over(board):
            if game_won(board, 'X'):
                display_board(board)
                print('X won!')
                exit()
            elif game_won(board, 'O'):
                display_board(board)
                print('O won!')
                exit()
            else:
                display_board(board)
                print('Tie!')
                exit()

main()
