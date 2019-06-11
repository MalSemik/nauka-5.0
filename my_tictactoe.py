size = 3


def create_board(size):
    board = [[" " for i in range(size)] for j in range(size)]
    return board


def print_board(board):
    pass


def numarate_cells():  # tu powinien przyjmować tablicę i sam se ją tak numerować, ale nie mogę wymyślic jak
    numerated_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return numerated_board


def select_walid_cell(board):
    while True:
        choice = int(input("Podaj komórkę"))
        i = (choice - 1) // 3
        j = (choice - 1) % 3
        print(i,j)
        chosen_cell = board[i][j]
        if chosen_cell == " ":
            return i, j
        else:
            print("Ta komórka jest już zajęta, spróbuj ponownie.")

select_walid_cell(create_board(3))
def select_player():  # tu coś zmieniającego z X na O... jakieś podanie imienia gracza czy cuś też by było
    pass
    return player_symbol
    # można stworzyć słownik playerów albo klasę


def player_move(board, player_symbol):  # to też nie działa
    i, j = select_walid_cell(board)
    board[i][j] = player_symbol
    return board


# test_board = [[" ", " ", 3], [" ", 5, 6], [7, 8, 9]]
# select_walid_cell(test_board, numarate_cells())

test_board = [["X", "O", "X"], ["X", "X", "X"], ["X", "O", "X"]]


def check_horizontal(board):
    for i in range(size):
        count_of_X = board[i].count("X")
        count_of_O = board[i].count("O")
        if count_of_X == size:  # ten fragment też by można jakoś uniezależnić, typu "claim winner"?
            print("Player X wins")  # tu jakieś ładne formatowanko zeby było Gosia wins, Rafał wins
        if count_of_O == size:
            print("Player O wins")


def check_vertical(board):
    for i in range(size):
        count_of_X = 0
        count_of_O = 0
        for j in range(len(board)):
            if board[j][i] == "X":
                count_of_X += 1
            if board[j][i] == "O":
                count_of_O += 1
        if count_of_X == 3:  # ten fragment też by można jakoś uniezależnić, typu "claim winner"?
            print("Player X wins")  # tu jakieś ładne formatowanko zeby było Gosia wins, Rafał wins
        if count_of_O == 3:
            print("Player O wins")
        else:
            continue


def check_diagonal_left_right(board):
    count_of_X = 0
    count_of_O = 0
    for i in range(size):
        if board[i][i] == "X":
            count_of_X += 1
        if board[i][i] == "O":
            count_of_O += 1
    if count_of_X == 3:  # ten fragment też by można jakoś uniezależnić, typu "claim winner"?
        print("Player X wins")  # tu jakieś ładne formatowanko zeby było Gosia wins, Rafał wins
    if count_of_O == 3:
        print("Player O wins")


def check_diagonal_right_left(board):
    count_of_X = 0
    count_of_O = 0
    for i in range(size):
        if board[i][size - i - 1] == "X":
            count_of_X += 1
        if board[i][size - i - 1] == "O":
            count_of_O += 1
    if count_of_X == 3:  # ten fragment też by można jakoś uniezależnić, typu "claim winner"?
        print("Player X wins")  # tu jakieś ładne formatowanko zeby było Gosia wins, Rafał wins
    if count_of_O == 3:
        print("Player O wins")


def check_if_full(board):
    counter = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != " ":
                counter += 1
    if counter == size * size:
        print("Remis")
        print("Game over")
        # play = False


# check_if_full(test_board)
check_diagonal_right_left(test_board)
