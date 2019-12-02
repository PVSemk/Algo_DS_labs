import time
import numpy as np
import sys


def find_minimal_operations_number(dimensions):
    matrix_amount = len(dimensions)
    cost_matrix = np.zeros((matrix_amount, matrix_amount))
    for chain_length in range(2, matrix_amount):
        for i in range(1, matrix_amount - chain_length + 1):
            j = i + chain_length - 1
            cost_matrix[i][j] = sys.maxsize
            for k in range(i, j):
                cost = cost_matrix[i, k] + cost_matrix[k + 1, j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cost < cost_matrix[i, j]:
                    cost_matrix[i, j] = cost
    return cost_matrix


def main():
    with open('input.txt', 'r') as file:
        data = np.asarray(list(map(int, file.read().split())))
    print(data)
    print(find_minimal_operations_number(data)[1, len(data) - 1])

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('\nTotal taken time: {:.5f}'.format(time.time() - start_time))
