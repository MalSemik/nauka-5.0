import PySimpleGUI as sg

size = 8

layout = [[sg.Button("", key=i) for i in range(size)] for j in range(size)]
#

# Create the Window
window = sg.Window('My calculator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event,values)
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break

window.close()

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[" " for i in range(size)] for j in range(size)]


    def print_board(board):
        for k in range(len(board)):
            print(board[k])

    def numarate_cells():  # tu powinien przyjmować tablicę i sam se ją tak numerować, ale nie mogę wymyślic jak
        numerated_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return numerated_board

    def check_horizontal(board, active_player):
        for i in range(size):
            count_of_active_player = board[i].count(active_player)
            if count_of_active_player == size:
                return True
        return False

    def check_vertical(board, active_player):
        for i in range(size):
            count_of_active_player = 0
            for j in range(len(board)):
                if board[j][i] == active_player:
                    count_of_active_player += 1
            if count_of_active_player == size:
                return True
        return False

    def CORRECT_check_vertical(board, active_player):
        for i in range(size):
            count_of_active_player = 0
            for j in range(len(board)):
                if board[j][i] == active_player:
                    count_of_active_player += 1
            if (
                    count_of_active_player == 3
            ):  # ten fragment też by można jakoś uniezależnić, typu "claim winner"?
                return True
        return False

    def check_diagonal_left_right(board, active_player):
        count_of_active_player = 0
        for i in range(size):
            if board[i][i] == active_player:
                count_of_active_player += 1
        if count_of_active_player == size:
            return True
        return False

    def check_diagonal_right_left(board, active_player):
        count_of_active_player = 0
        for i in range(size):
            if board[i][size - i - 1] == active_player:
                count_of_active_player += 1
        if count_of_active_player == size:
            return True
        return False

    def check_if_full(board):
        counter = 0
        for i in range(size):
            for j in range(size):
                if board[i][j] != " ":
                    counter += 1
        if counter == size * size:
            print("Remis")
            print("Game over")
            return True
        return False

    def check_all(board, active_player):
        return (
                check_horizontal(board, active_player)
                or check_vertical(board, active_player)
                or check_diagonal_right_left(board, active_player)
                or check_diagonal_left_right(board, active_player)
        )


class HumanPlayer:
    pass


class ComputerPlayer:
    pass
