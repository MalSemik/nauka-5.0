import random

size = 3


def create_board(size):
    board = [[" " for i in range(size)] for j in range(size)]
    return board


def print_board(board):
    for k in range(len(board)):
        print(board[k])


def numarate_cells():  # tu powinien przyjmować tablicę i sam se ją tak numerować, ale nie mogę wymyślic jak
    numerated_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return numerated_board


def select_walid_cell(board):
    while True:
        choice = int(input("Podaj komórkę"))
        i = (choice - 1) // 3
        j = (choice - 1) % 3
        # print(i, j)
        chosen_cell = board[i][j]
        if chosen_cell == " ":
            return i, j
        else:
            print("Ta komórka jest już zajęta, spróbuj ponownie.")


def name_players():
    players = {}
    players["O"] = input("Podaj imię gracza O: ")
    players["X"] = input("Podaj imię gracza X: ")
    return players


def select_player_who_starts(players: dict):
    active_player = random.choice(list(players.keys()))
    print("Zaczyna ", players[active_player])
    return active_player


def switch_players(active_player, players):
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"
    print("Ruch wykonuje", players[active_player])
    return active_player


def player_move(board, active_player):
    i, j = select_walid_cell(board)
    board[i][j] = active_player
    print_board(board)
    return board


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


def check_if_full(board, active_player):
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


def main():
    players = name_players()
    active_player = select_player_who_starts(players)
    board = create_board(3)
    print("Wstaw symbol wybierając miejsce od 1 do 9")
    print_board(numarate_cells())
    while True:
        player_move(board, active_player)
        if check_all(board, active_player) == True:
            print("Wygrywa", players[active_player])
            break
        elif check_if_full(board, active_player) == True:
            break
        else:
            active_player = switch_players(active_player, players)


main()
