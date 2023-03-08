from tictactoe import *
X = "X"
O = "O"
EMPTY = None
b = [[X, EMPTY, EMPTY],
        [EMPTY, O, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

b1 = [[X, EMPTY, EMPTY],
        [X, O, EMPTY],
        [X, O, EMPTY]]

b2 = [[X, X, EMPTY],
        [O, O, O],
        [EMPTY, EMPTY, X]]

b3 = [[X, X, O],
        [X, O, O],
        [X, O, X]]

b4 = [[X, O, X],
        [X, O, O],
        [O, X, X]]

print(player(b), actions(b), winner(b), terminal(b), utility(b))
print(player(b1), actions(b1), winner(b1), terminal(b1), utility(b1))
print(player(b2), actions(b2), winner(b2), terminal(b2), utility(b2))
print(player(b3), actions(b3), winner(b3), terminal(b3), utility(b3))
print(player(b4), actions(b4), winner(b4), terminal(b4), utility(b4))
