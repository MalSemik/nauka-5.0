tests = int(input())
for i in range(tests):
    clues = int(input())
    north = 0
    east = 0
    for j in range(clues):
        clue = input()
        clue = clue.split()
        clue = [int(clue[i]) for i in range(len(clue))]
        direction = clue[0]
        steps = clue[1]
        if direction == 0:
            north = north + steps
        elif direction == 1:
            north -= steps
        elif direction == 2:
            east += steps
        elif direction == 3:
            east -= steps

    if north == 0 and east == 0:
        print("studnia")
    elif north < 0:
        print("1", -north)
    elif north > 0:
        print("0", north)

    if east < 0:
        print("3", -east)
    elif east > 0:
        print("2", east)

