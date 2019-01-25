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

    def checkEndGame(self):
        if self.checkCol() and self.checkDia() or self.checkRow():
            return True
        for move in self._state:
            if move == " " or move == "":
                return False
        return True

    def checkRow(self):
        state = self._state
        for i in range(3):
            if (state[3 * i] == state[3 * i + 1] == state[3 * i + 2]) and state[3 * i] != " ":
                return True
        return False

    def checkCol(self):
        state = self._state
        for i in range(3):
            if state[i] == state[i + 3] == state[i + 6] and state[i] != " ":
                return True
        return False

    def checkDia(self):
        state = self._state
        if ((state[0] == state[4] == state[8]) or (state[2] == state[4] == state[6])) and state[4] != " ":
            return True
        return False


if __name__ == "__main__":
    ticTacToe = TicTacToe()
    ticTacToe.importBoard(["X", "O", "X", "X", "", "O", "X", "X", "X"])
    print("checkEndGame", ticTacToe.checkEndGame())
    move = 9
    print(f"validateMove({move})", ticTacToe.validateMove(9))
