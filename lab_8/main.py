from collections import namedtuple, deque
from itertools import product
import time
import numpy as np

def Li_algorithm(matrix, num_grenades):
    # delta_coord = list(product([-1, 0, 1], repeat=2))
    delta_coord = ((0, -1), (0, 1), (1, 0), (-1, 0))
    # delta_coord.remove((0, 0))
    cells_handling_queue = deque()
    matrix[0][0] = 0
    matrix_height, matrix_width, matrix_depth = matrix.shape
    cells_handling_queue.append((0, 0, num_grenades))
    while cells_handling_queue:
        coordinates = cells_handling_queue.popleft()
        for delta in delta_coord:
            new_x = coordinates[0] + delta[0]
            new_y = coordinates[1] + delta[1]
            num_grenades = coordinates[2]
            if new_x == new_y == 0:
                continue
            if 0 <= new_x < matrix_height and 0 <= new_y < matrix_width:
                if matrix[new_x, new_y, num_grenades] == -1 and num_grenades >= 1:
                    if matrix[new_x, new_y, num_grenades - 1] == -1 or matrix[new_x, new_y, num_grenades - 1] > matrix[coordinates[0], coordinates[1], num_grenades] + 1:
                        cells_handling_queue.append((new_x, new_y, num_grenades - 1))
                        matrix[new_x, new_y, num_grenades - 1] = matrix[coordinates[0], coordinates[1], num_grenades] + 1
                    continue
                elif not matrix[new_x, new_y, num_grenades] or matrix[new_x, new_y, num_grenades] > matrix[coordinates[0], coordinates[1], num_grenades] + 1:
                    cells_handling_queue.append((new_x, new_y, num_grenades))
                    matrix[new_x, new_y, num_grenades] = matrix[coordinates[0], coordinates[1], num_grenades] + 1
    return matrix


def main():
    num_grenades = 2
    with open('lab_1.txt') as file:
        try:
            content = [list(map(int, line.split())) for line in file.readlines()]
        except ValueError:
            print('Inputs should be numbers')
    nd_content = np.repeat(np.asarray(content)[:, :, np.newaxis], num_grenades + 1, axis=-1)
    nd_content[nd_content == 1] = -1
    matrix = Li_algorithm(nd_content, num_grenades)
    non_zero = np.nonzero(matrix[-1, -1, :])
    steps = np.min(matrix[-1, -1, non_zero])
    print("You should spent {} steps".format(steps))
    # if final_steps_number != -1:
    #     print('You should spend at least {} steps'.format(final_steps_number))
    # else:
    #     print('Sorry')




if __name__ == '__main__':
    start = time.time()
    main()
    print('Taken time: {:.5f}'.format(time.time() - start))
