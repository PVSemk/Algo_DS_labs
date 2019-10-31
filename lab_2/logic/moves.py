from copy import deepcopy


def move_down(state):
    x, y = state.empty_cell.x, state.empty_cell.y
    state.swap_with_empty((x, y), (x + 1, y), 'Down')
    return None


def move_up(state):
    x, y = state.empty_cell.x, state.empty_cell.y
    state.swap_with_empty((x, y), (x - 1, y), 'Up')
    return None


def move_left(state):
    x, y = state.empty_cell.x, state.empty_cell.y
    state.swap_with_empty((x, y), (x, y - 1), 'Left')
    return None


def move_right(state):
    x, y = state.empty_cell.x, state.empty_cell.y
    state.swap_with_empty((x, y), (x, y + 1), 'Right')
    return None


def make_moves(state):
    next_states = []
    moves, shifts = [move_left, move_right, move_up, move_down], [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for move, shift in zip(moves, shifts):
        tmp = deepcopy(state)
        tmp.parent = state
        if check_move_possibility(tmp.empty_cell, shift):
            move(tmp)
            next_states.append(tmp)
    return next_states


def check_move_possibility(empty_loc, new_empty_loc):
    return 0 <= empty_loc[0] + new_empty_loc[0] < 3 and\
           0 <= empty_loc[1] + new_empty_loc[1] < 3
