import time
from collections import deque
from logic import make_moves, BoardState, initialize_board
import sys


def find_solution(start_state, target_state):
    node_counter = 1
    bfs_queue = deque()
    explored = set()
    bfs_queue.append(start_state)
    explored.add(repr(start_state))
    while bfs_queue:
        current_state = bfs_queue.popleft()
        if current_state == target_state:
            print('Proceeded {} nodes'.format(node_counter))
            return backtrace(current_state)

        for move in make_moves(current_state):
            if node_counter % 7000 == 0:
                print('Queue size: {}\tSet of explored nodes amount: {}\tNodes proceeded: {}'
                      .format(len(bfs_queue), len(explored), node_counter))
            node_counter += 1
            if repr(move) not in explored:
                bfs_queue.append(move)
                explored.add(repr(move))

    return 0


def backtrace(state):
    path = []
    while state.parent is not None:
        path.append(state.move_from_parent)
        state = state.parent
    return reversed(path)


def main():
    with open(sys.path[0] + '/in.txt') as file:
        shuffled_word = file.readline()
    initial_state = BoardState(*initialize_board(shuffled_word))
    print(initial_state)
    target_state = BoardState(*initialize_board('xameleon'))
    print(target_state)
    solution = find_solution(initial_state, target_state)
    if solution:
        print(*solution)
        return 0
    else:
        return -1


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Taken time: {:.5f}'.format(time.time() - start_time))



