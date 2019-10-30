from collections import namedtuple

EmptyLocation = namedtuple('EmptyLocation', 'x y')


class BoardState:
    def __init__(self, state, empty_cell, parent=None, move_from_parent=None):
        self.state = state
        self.parent = parent
        self.empty_cell = empty_cell
        self.move_from_parent = move_from_parent

    def __repr__(self):
        return str(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i][j], end=' ')
            print('\n')
        return ''

    def swap(self, pair_a, pair_b):
        self.state[pair_a[0]][pair_a[1]], self.state[pair_b[0]][pair_b[1]] = self.state[pair_b[0]][pair_b[1]],\
                                                                             self.state[pair_a[0]][pair_a[1]]
        return None


def initialize_board(shuffled_word):
    board = [['_' for j in range(3)] for i in range(3)]
    empty_cell = EmptyLocation(2, 2)
    for idx, letter in enumerate(shuffled_word):
        row = idx // 3
        col = idx % 3
        board[row][col] = shuffled_word[idx]
        if letter == '_':
            empty_cell = EmptyLocation(row, col)
    return board, empty_cell