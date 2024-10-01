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

    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    if x_count == o_count:
        return 'X'
    
    else:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_choices = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_choices.add((i, j))

    return action_choices


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """


    if action not in actions(board=board):
        raise Exception('Invalid action')
    
    mover = player(board=board)
    i, j = action
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = mover

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    else:
        return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board=board) is not None:
        return True
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
            
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board=board) == X:
        return 1
    
    elif winner(board=board) == O:
        return -1
    
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board=board):
        return None
    
    choice = ()
    
    if player(board=board) == X:
        maxVal = -math.inf
        for action in actions(board):
            state = result(board, action)
            # maxVal = max(maxVal, min_value(state))
            if min_value(state) > maxVal:
                maxVal = min_value(state)
                choice = action

        return choice
    
    else:
        minVal = math.inf
        for action in actions(board):
            state = result(board, action)
            # minVal = min(minVal, max_value(state))
            if max_value(state) < minVal:
                minVal = max_value(state)
                choice = action

        return choice
    

    
def max_value(board):
    if terminal(board=board):
        return utility(board=board)
    
    maxVal = -math.inf
    for action in actions(board):
        state = result(board, action)
        maxVal = max(maxVal, min_value(state))

    return maxVal

def min_value(board):
    if terminal(board=board):
        return utility(board=board)
    
    minVal = math.inf
    for action in actions(board):
        state = result(board, action)
        minVal = min(minVal, max_value(state))

    return minVal





