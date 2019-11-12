import sys
import time

target_subset = []
minimal_subset = []
def backtracking_search(data, target_number, partial_sum, next_idx, remaining_sum):  # Algorithm from https://www.cise.ufl.edu/~sahni/papers/computingPartitions.pdf
    global target_subset, minimal_subset

    if partial_sum + remaining_sum == target_number:
        target_set = target_subset[:]
        target_set.extend(range(next_idx, len(data)))
        if len(target_set) < len(minimal_subset):
            minimal_subset = [data[idx] for idx in target_set]
        if next_idx < len(data) - 1:
            backtracking_search(data, target_number, partial_sum, next_idx + 1, remaining_sum - data[next_idx])
        else:
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
        start_sort = time.time()
        data = {len(line.rstrip().split()): sorted(map(int, line.rstrip().split())) for line in data}
        print('Sorting took {}'.format(time.time() - start_sort))
    for length, numbers in list(data.items()):
        start = time.time()
        count = 0
        minimal_subset = numbers[:]
        target_subset = []
        backtracking_search(numbers, 18, 0, 0, sum(numbers))
        stop = time.time()
        print('Minimal subset: {}; Total numbers in data: {}; Time for searching: {}'. format(minimal_subset, length, stop - start))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Total taken time: {:.5f}'.format(time.time() - start_time))