import sys
import os
import time
from copy import deepcopy

target_subset = []
minimal_subset = []
def backtracking_search(data, target_number, partial_sum, next_idx, remaining_sum):  # Algorithm from https://www.cise.ufl.edu/~sahni/papers/computingPartitions.pdf
    global target_subset, minimal_subset

    # partial_sum = sum([data[idx] for idx in target_subset]) if target_subset else 0
    # print(target_subset)
    # if target_subset == [5, 8] or target_subset == [6, 7]:
    # print("SADSAJDSASDJLASKLDASJD")
    # if partial_sum + remaining_sum < target_number:
    #     return
    if partial_sum + remaining_sum == target_number:
        target_set = target_subset[:]
        target_set.extend(range(next_idx, len(data)))
        # print('\t', target_set)
        if len(target_set) < len(minimal_subset):
            minimal_subset = [data[idx] for idx in target_set]
        return
    if partial_sum + data[next_idx] > target_number:
        return
    if partial_sum + data[next_idx] == target_number:
        if len(target_subset) < len(minimal_subset):
            minimal_subset = [data[idx] for idx in target_subset]
            minimal_subset.append(data[next_idx])
        if next_idx < len(data) - 1:
            backtracking_search(data, target_number, partial_sum, next_idx + 1, remaining_sum - data[next_idx])
        else:
            return
    if next_idx < len(data) - 1:
        target_subset.append(next_idx)
        backtracking_search(data, target_number, partial_sum + data[next_idx], next_idx + 1, remaining_sum - data[next_idx])
        target_subset.pop()
    else:
        return
    backtracking_search(data, target_number, partial_sum, next_idx + 1, remaining_sum - data[next_idx])
    return


def main():
    global minimal_subset, target_subset, count
    with open(sys.path[0] + '/in.txt') as file:
        data = file.readlines()
        data = {len(line.rstrip().split()): sorted(map(int, line.rstrip().split())) for line in data}  # Takes 3.5e-4 sec
    for length, numbers in list(data.items()):
        count = 0
        # print(numbers)
        minimal_subset = numbers[:]
        target_subset = []
        # print('\t', len(numbers))
        # print(numbers)
        backtracking_search(numbers, 18, 0, 0, sum(numbers))
        # print(count)
        summ = 0
        # for i in output:
        #     summ += numbers[i]
        print(minimal_subset, sum(minimal_subset))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Taken time: {:.5f}'.format(time.time() - start_time))