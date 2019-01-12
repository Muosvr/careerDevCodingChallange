#!/bin/python3


def drawBoard(arr):
    print(f" {arr[0]} | {arr[1]} | {arr[2]}")
    for i in range(1, 3):
        print("---+---+---")
        print(f" {arr[3 * i + 0]} | {arr[3 * i + 1]} | {arr[3 * i + 2]}")


def checkRows(state):
    for i in range(3):
        if (state[3 * i] == state[3 * i + 1] == state[3 * i + 2]) and state[3 * i] != " ":
            return True
    return False


def checkCol(state):
    for i in range(3):
        if state[i] == state[i + 3] == state[i + 6] and state[i] != " ":
            return True
    return False


def checkDia(state):
    if ((state[0] == state[4] == state[8]) or (state[2] == state[4] == state[6])) and state[4] != " ":
        return True
    return False


def checkTie(state):
    for space in state:
        if space == " ":
            return False
    return True


if __name__ == "__main__":
    import sys
    print(sys.version)
    state = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    drawBoard(state)

    X = True
    while True:
        if X:
            print("Player X enter where to place your piece:")
        else:
            print("Player O enter where to place your piece:")
        print(" 0 | 1 | 2 ")
        print("-----------")
        print(" 3 | 4 | 5 ")
        print("-----------")
        print(" 6 | 7 | 8 ")
        index = int(input("index: "))

        if X and state[index] == " ":
            state[index] = "X"
            drawBoard(state)
        elif not X and state[index] == " ":
            state[index] = "O"
            drawBoard(state)
        else:
            print("Cannot place there")
            drawBoard(state)
        if checkRows(state) or checkCol(state) or checkDia(state):
            if X:
                print("Player X wins")
            else:
                print("Player O wins")
            break
        if checkTie(state):
            print("It's a tie")
            break
        X = not X
