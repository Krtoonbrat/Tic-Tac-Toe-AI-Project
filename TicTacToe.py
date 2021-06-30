import re
import copy
import math
class TicTacToe():
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.xWin = False
        self.oWin = False
        self.draw = False
        self.gameOver = False
        self.endStatesCount = 0

    def getGameOver(self, board):
        self.gameOver = self.checkGameOver(board)
        return self.gameOver

    def getGameEndState(self):
        if self.xWin:
            return 1
        elif self.oWin:
            return -1
        elif self.draw:
            return 0

    def getBoard(self):
        return self.board
    
    def getPossibleMoves(self, board):
        moves = []
        for row in range(3):
            for column in range(3):
                if type(board[row][column]) == int:
                    moves.append([row, column])
        return moves

    def aiMakeMove(self, move, board, isMaximizer):
        if isMaximizer:
            board[move[0]][move[1]] = "X"
        else:
            board[move[0]][move[1]] = "O"

    def undoMove(self, board, move):
        if move[0] == 0:
            if move[1] == 0:
                undo = 1
            elif move[1] == 1:
                undo = 2
            elif move[1] == 2:
                undo = 3
        elif move[0] == 1:
            if move[1] == 0:
                undo = 4
            elif move[1] == 1:
                undo = 5
            elif move[1] == 2:
                undo = 6
        elif move[0] == 2:
            if move[1] == 0:
                undo = 7
            elif move[1] == 1:
                undo = 8
            elif move[1] == 2:
                undo = 9
        
        board[move[0]][move[1]] = undo
        return undo

    def resetGameStates(self):
        self.xWin = False
        self.oWin = False
        self.draw = False

    # draws the board by looping through three times and drawing each row
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

    # goes throught the process of a turn
    # takes the player whose turn it is as input
    # returns if the game is over or not
    def turn(self, player):

        # tell the user whose turn it is and how to input their move
        print("Your turn.  Please input a number 1-9.")
        
        move = input("Your move? ")

        # if the user inputted a valid spot on the board, we can move
        # through the move process
        if re.fullmatch("[1-9]", move):
            # turning the move into board coordinates
            # first is row, second is column
            move = [(int(move) - 1) // 3, (int(move) - 1) % 3]

            # if there is not a piece at the move position already
            # the player's move will be placed there
            # if not, player is informed and asked for more input
            if type(self.board[move[0]][move[1]]) == int:
                self.board[move[0]][move[1]] = player
            else:
                print("Cannot make that move, there is a piece there already.")
                self.turn(player)
        else:
            print("Please input a valid board position.")
            self.turn(player)

        self.gameOver = self.checkGameOver(self.board)

        return self.gameOver

    # checks if the game is over by looping through the possible
    # vertical and horizontal win states, then checking
    # the two diagonal win states
    # if nobody has won yet, it checks for a draw
    def checkGameOver(self, board):
        for player in ["X", "O"]:
            # check vertical and horizontal
            for check in range(3):
                if board[check][0] == player and board[check][1] == player and board[check][2] == player:
                    if player == "X":
                        self.xWin = True
                    else:
                        self.oWin = True
                    return True

                if board[0][check] == player and board[1][check] == player and board[2][check] == player:
                    if player == "X":
                        self.xWin = True
                    else:
                        self.oWin = True
                    return True
            
            # check diagonals
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                if player == "X":
                    self.xWin = True
                else:
                    self.oWin = True
                return True

            elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
                if player == "X":
                    self.xWin = True
                else:
                    self.oWin = True
                return True

        # check draw
        for row in range(3):
            for column in range(3):
                if type(board[row][column]) == int:
                    return False
        self.draw = True
        return True

# AI uses the minimax algorithm in order to find the best move
class AI():
    # sets up the variables needed for the AI
    def setup(self):
        global board
        global psudoToe
        board = copy.deepcopy(game.getBoard())
        psudoToe = TicTacToe()

    # the actual minimax algorithm
    # a win is scored as 1, loss as -1, and draw as 0
    def minimax(self, isMaximizer, gameboard, alpha, beta):
        # first check if the current board state is a game over
        # if it is score it and add it to the count
        if psudoToe.getGameOver(gameboard):
            psudoToe.endStatesCount += 1
            return psudoToe.getGameEndState()

        # the AI will find all possible moves from the current board
        # state, then make the moves, score the end state resulting
        # from the move, then undo the move and try the next one
        scores = []
        if isMaximizer:
            maxScore = -math.inf
            for moves in psudoToe.getPossibleMoves(gameboard):
                psudoToe.aiMakeMove(moves, gameboard, isMaximizer)
                score = self.minimax(False, copy.deepcopy(gameboard), alpha, beta)
                maxScore = max(score, maxScore)
                alpha = max(score, alpha)
                if beta <= alpha:
                    break
                psudoToe.undoMove(gameboard, moves)
                psudoToe.resetGameStates()
            return maxScore
        else:
            minScore = math.inf
            for moves in psudoToe.getPossibleMoves(gameboard):
                psudoToe.aiMakeMove(moves, gameboard, isMaximizer)
                score = self.minimax(True, copy.deepcopy(gameboard), alpha, beta)
                minScore = min(score, minScore)
                beta = min(score, beta)
                if beta <= alpha:
                    break
                psudoToe.undoMove(gameboard, moves)
                psudoToe.resetGameStates()
            return minScore

    # go starts the minimax process and handels finding the best move
    # then actually makes that move
    def go(self):
        bestScore = -math.inf
        bestMove = None
        for moves in psudoToe.getPossibleMoves(board):
            psudoToe.aiMakeMove(moves, board, True)
            score = self.minimax(False, copy.deepcopy(board), -math.inf, math.inf)
            psudoToe.undoMove(board, moves)
            psudoToe.resetGameStates()
            if score > bestScore:
                bestScore = score
                bestMove = moves
        print(psudoToe.endStatesCount, " total end states explored.")
        print("Playing an X at {}".format(psudoToe.undoMove(board, bestMove)))
        game.aiMakeMove(bestMove, game.board, True)

game = TicTacToe()
game.drawBoard()
player = "O"
ai = AI()
while True:
    print("AI's turn.")
    ai.setup()
    ai.go()
    game.drawBoard()
    if game.checkGameOver(game.board):
        if game.getGameEndState() == 1:
            print("Ha Ha you lose!")
            break
        elif game.getGameEndState() == 0:
            print("It's a draw.")
            break
    else:
        if game.turn(player):
            if game.getGameEndState() == -1:
                print("Impossible.  You won.")
                break
            elif game.getGameEndState() == 0:
                print("It's a draw.")
                break
    game.drawBoard()