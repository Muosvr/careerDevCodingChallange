class TicTacToe:
    def __init__(self):
        print("Let's play Tic Tac Toe!")
        self._state = [" "] * 9
        self.drawBoard()

    def importBoard(self, state):

        self.processEmptyString(state)
        self._state = state
        print("New state imported")
        self.drawBoard()

    def drawBoard(self):
        arr = self._state
        self.processEmptyString(arr)
        print(f" {arr[0]} | {arr[1]} | {arr[2]}")

        for i in range(1, 3):
            print("---+---+---")
            print(f" {arr[3 * i + 0]} | {arr[3 * i + 1]} | {arr[3 * i + 2]}")

    def processEmptyString(self, arr):
        for i in range(len(arr)):
            if arr[i] == "":
                arr[i] = " "

    def validateMove(self, move):
        if move > 8:
            return False
        elif self._state[move] == "X" or self._state[move] == "O":
            return False
        else:
            return True


if __name__ == "__main__":
    ticTacToe = TicTacToe()
    ticTacToe.importBoard(["", "", "X", "X", "O", "", "", "", "X"])
    print(ticTacToe.validateMove(9))
