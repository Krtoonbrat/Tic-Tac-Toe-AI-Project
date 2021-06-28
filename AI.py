from TicTacToe import TicTacToe, game
import copy
import math

def setup():
    global board
    global psudoToe
    board = copy.deepcopy(game.getBoard())
    psudoToe = TicTacToe()

def minimax(isMaximizer, board):
    if psudoToe.getGameOver(board):
        return psudoToe.getGameEndState()

    scores = []
    if isMaximizer:
        for moves in psudoToe.getPossibleMoves(board):
            psudoToe.aiMakeMove(moves, board, isMaximizer)
            scores.append(minimax(False, copy.deepcopy(board)))
            psudoToe.undoMove(board, moves)
            psudoToe.resetGameStates
        return max(scores)
    else:
        for moves in psudoToe.getPossibleMoves(board):
            psudoToe.aiMakeMove(moves, board, isMaximizer)
            scores.append(minimax(True, copy.deepcopy(board)))
            psudoToe.undoMove(board, moves)
            psudoToe.resetGameStates()
        return min(scores)

def go():
    bestScore = -math.inf
    bestMove = None
    for moves in psudoToe.getPossibleMoves(board):
        psudoToe.aiMakeMove(moves, board, True)
        score = minimax(True, board)
        psudoToe.undoMove(board, moves)
        psudoToe.resetGameStates()
        if score > bestScore:
            bestScore = score
            bestMove = moves
    game.aiMakeMove(bestMove, game.board)
