from .board import BoardState, EmptyLocation
from copy import deepcopy


def make_moves(state):
    next_states = []
    empty_row = state.empty_cell.x
    empty_col = state.empty_cell.y
    old_coordinates = (empty_row, empty_col)

    left = (empty_row, empty_col - 1)
    right = (empty_row, empty_col + 1)
    up = (empty_row - 1, empty_col)
    down = (empty_row + 1, empty_col)

    for new_coordinates, direction in zip([left, up, right, down], ['Left', 'Up', 'Right', 'Down']):
        if 0 <= new_coordinates[0] < 3 and 0 <= new_coordinates[1] < 3:
            new_state = deepcopy(state)
            new_state.parent = state
            new_state.swap_with_empty(old_coordinates, new_coordinates, direction)
            next_states.append(new_state)

    return next_states
