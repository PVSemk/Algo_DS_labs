from copy import deepcopy
from collections import deque
from .board import EmptyLocation


def move_down(state):
    x, y = state.empty_cell.x, state.empty_cell.y
    state.swap((x, y), (x + 1, y))
    state.move_from_parent = 'Down'
    state.empty_cell = EmptyLocation(x + 1, y)
    return None


def move_up(state):
    x, y = state.empty_cell.x, state.empty_cell.y
    state.swap((x, y), (x - 1, y))
    state.move_from_parent = 'Up'
    state.empty_cell = EmptyLocation(x-1, y)
    return None


def move_left(state):
    x, y = state.empty_cell.x, state.empty_cell.y
    state.swap((x, y), (x, y - 1))
    state.move_from_parent = 'Left'
    state.empty_cell = EmptyLocation(x, y - 1)
    return None


def move_right(state):
    x, y = state.empty_cell.x, state.empty_cell.y
    state.swap((x, y), (x, y + 1))
    state.move_from_parent = 'Right'
    state.empty_cell = EmptyLocation(x, y + 1)
    return None


def make_moves(state):
    next_states = []
    tmp = deepcopy(state)
    tmp.parent = state
    if 0 <= state.empty_cell.x < 2:
        move_down(tmp)
        next_states.append(tmp)
        tmp = deepcopy(state)
        tmp.parent = state
    if 1 <= state.empty_cell.x < 3:
        move_up(tmp)
        next_states.append(tmp)
        tmp = deepcopy(state)
        tmp.parent = state
    if 0 <= state.empty_cell.y < 2:
        move_right(tmp)
        next_states.append(tmp)
        tmp = deepcopy(state)
        tmp.parent = state
    if 1 <= state.empty_cell.y < 3:
        move_left(tmp)
        next_states.append(tmp)
    return next_states
