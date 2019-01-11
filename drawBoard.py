#!/bin/python3


def drawBoard(arr):
    print(f" {arr[0]} | {arr[1]} | {arr[2]}")
    for i in range(1, 3):
        print("---+---+---")
        print(f" {arr[3 * i + 0]} | {arr[3 * i + 1]} | {arr[3 * i + 2]}")


if __name__ == "__main__":
    import sys
    print(sys.version)
    drawBoard([0, 1, 2, 3, 4, 5, 6, 7, 8])
