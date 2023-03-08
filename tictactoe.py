"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xs = 0
    os = 0
    for i in board:
        xs += i.count('X')
        os += i.count('O')
    if xs > os:
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                act.add( (i,j) )
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    if not board[action[0]][action[1]]:
        board_copy[action[0]][action[1]] = player(board)
        return board_copy
    else:
        raise Exception()


def conditionals(board, func):
    #horizontal win
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] != None:
                return func(board[i][0])
    #vertical win
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] != None:
                return func(board[0][i])
    #diagonal win
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != None:
            return func(board[0][0])
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] != None:
            return func(board[0][2])
    else:
        return func(None)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #checking if game is in progress
    if not terminal(board):
        return None
    else:
        return conditionals(board, lambda x: x)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    row_Nones = list()
    for i in board:
        row_Nones.append(i.count(None))
    if not any(row_Nones):
        return True
    else:
        return conditionals(board, lambda x:bool(x))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    s = winner(board)
    if s == 'X':
        return 1
    elif s == 'O':
        return -1
    else:
        return 0


def max_ut(board):
    if terminal(board):
        return utility(board)
    v = -1000
    for action in actions(board):
        v = max(v, min_ut(result(board, action)))
    return v


def min_ut(board):
    if terminal(board):
        return utility(board)
    v = 1000
    for action in actions(board):
        v = min(v, max_ut(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        li = list(actions(board))
        li_ut = list()
        if player(board) == 'X':
            for action in li:
                li_ut.append( min_ut( result(board, action) ) )
            return li[li_ut.index(max(li_ut))]
        else:
            for action in li:
                li_ut.append( max_ut( result(board, action) ) )
            return li[li_ut.index(min(li_ut))]
