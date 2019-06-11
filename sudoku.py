def read_board_from_file():
    with open("sepuku_01.txt","r") as source_file:
        # board = []
        # for line in source_file:
        #     row = [int(item) for item in line.split()]
        #     board.append(row)
        board = [[int(item) for item in line.split()] for line in source_file]
        return board

def print_board(board):
    for line in board:
        row = [str(item) if item != 0 else " " for item in line ]
        print(" ".join(row))



