class TicTacToe():
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def drawBoard(self):
        for i in range(3):
            for x in range(2):
                print("       |", end = "")
            print("")

            print("   {}   |   {}   |   {}   ".format(self.board[i][0], self.board[i][1], self.board[i][2]))

            for x in range(2):
                print("       |", end = "")
            print("")

            if i != 2:
                print("-"*23)

    