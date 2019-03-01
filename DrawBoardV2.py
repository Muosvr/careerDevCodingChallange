def DrawBoard(x, y):
    ROWHEIGHT = 1
    for _ in range(x):
        for _ in range(y):
            print("+ == ", end="")
        print("+")
        for _ in range(y):
            print("|    ", end="")
        print("|")
    for _ in range(y):
        print("+ == ", end="")
    print("+")


if __name__ == "__main__":
    DrawBoard(3, 4)
