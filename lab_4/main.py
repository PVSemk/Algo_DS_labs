import sys
import time

def count_sort(array):
    max_range = max(array) + 1
    counters = [0 for i in range(0, max_range)]
    sorted_array = [0 for i in range(0, len(array))]
    for i in range(len(array)):
        counters[array[i]] += 1
    for j in range(1, max_range):
        counters[j] += counters[j-1]
    for i in range(len(array) - 1, -1, -1):
        counters[array[i]] -= 1
        sorted_array[counters[array[i]]] = array[i]
    return sorted_array

def main():
    array = [1, 4, 0, 12, 3, 2, 1, 7, 7, 5, 4]
    print(count_sort(array))

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Total taken time: {:.5f}'.format(time.time() - start_time))