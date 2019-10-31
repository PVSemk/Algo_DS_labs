from .board import BoardState, EmptyLocation


def make_moves(state):
    next_states = []
    empty_row = state.empty_cell.x
    empty_col = state.empty_cell.y

    left = (empty_row, empty_col - 1)
    right = (empty_row, empty_col + 1)
    up = (empty_row - 1, empty_col)
    down = (empty_row + 1, empty_col)

    for new_coordinates, direction in zip([left, up, right, down], ['Left', 'Up', 'Right', 'Down']):
        (new_empty_row, new_empty_col) = new_coordinates

        if 0 <= new_empty_row < 3 and 0 <= new_empty_col < 3:
            new_state = [r[:] for r in state.state]  # Taking slice in order to copy values, not reference to list
            new_state[empty_row][empty_col], new_state[new_empty_row][new_empty_col] =  \
                new_state[new_empty_row][new_empty_col], state.state[empty_row][empty_col]

            next_states.append(BoardState(new_state, EmptyLocation(new_empty_row, new_empty_col), state, direction))

    return next_states
