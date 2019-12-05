import time
import numpy as np


def find_number_of_paths(matrix):
    answers = [[0 for _ in range(matrix.shape[1])] for _ in range(matrix.shape[0])]
    for i in range(matrix.shape[0]):
        answers[i][0] = 1
    for j in range(matrix.shape[1]):
        answers[0][j] = 1
    for i in range(1, matrix.shape[0]):
        for j in range(1, matrix.shape[1]):
            answers[i][j] = answers[i - 1][j] + answers[i][j - 1]
    return answers


def main():
    fpath = 'bug_1.txt'
    with open(fpath, 'r') as file:
        data = file.readlines()
    rows = len(data)
    cols = len(data[0].rstrip())
    matrix = np.zeros((rows, cols))
    answers = find_number_of_paths(matrix)
    print('Total number of paths in matrix {}x{} is {}'.format(rows, cols, answers[-1][-1]))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('\nTotal taken time: {:.5f}'.format(time.time() - start_time))
