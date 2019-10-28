from utils.utils import parse_arguments
from collections import namedtuple, deque
import time

def Li_algorithm(matrix, start_x, start_y, finish_x, finish_y):
    delta_coord = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    cells_handling_queue = deque()
    steps = 0
    matrix[start_x][start_y] = steps
    matrix_width = len(matrix[0])
    matrix_height = len(matrix)
    cells_handling_queue.append((start_x, start_y))
    while cells_handling_queue:
        coordinates = cells_handling_queue.popleft()
        if matrix[coordinates[0]][coordinates[1]] == steps + 1:
            steps = steps + 1
        for delta in delta_coord:
            new_x = coordinates[0] + delta[0]
            new_y = coordinates[1] + delta[1]
            if 0 <= new_x < matrix_height and 0 <= new_y < matrix_width and matrix[new_x][new_y] == -1:
                cells_handling_queue.append((new_x, new_y))
                matrix[new_x][new_y] = steps+1
            if matrix[finish_x][finish_y] != -1:
                return matrix[finish_x][finish_y], matrix

def main(args):
    Coordinates = namedtuple('Coordinates', 'height width start_x start_y finish_x finish_y')
    with open(args.infile) as file:
        try:
            content = list(map(int, file.read().split()))
        except ValueError:
            print('Inputs should be numbers')
    coordinates = Coordinates(*content)
    matrix = [[-1 for j in range(coordinates.width)] for i in range(coordinates.height)]
    import numpy as np
    print(np.asarray(matrix))
    final_steps_number, matrix = Li_algorithm(matrix,
                          coordinates.start_x,
                          coordinates.start_y,
                          coordinates.finish_x,
                          coordinates.finish_y
                          )
    print(np.asarray(matrix))
    print('You should spend at least {} '
          'steps in order to reach {} from {}'.format(final_steps_number,
                                                      coordinates[4:6],
                                                      coordinates[2:4]
                                                      )
          )
    with open(args.outfile, 'w') as file:
        file.write(str(final_steps_number))

if __name__ == '__main__':
    start = time.time()
    arguments = parse_arguments()
    main(arguments)
    print('Taken time: {}'.format(time.time() - start))