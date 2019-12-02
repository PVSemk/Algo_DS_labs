import time
from random import randint


def quicksort(array, low, high):
    if low < high:
        idx = partitition(array, low, high)
        quicksort(array, low, idx - 1)
        quicksort(array, idx + 1, high)


def partitition(array, low, high):
    rand_int = randint(low, high)
    pivot = array[rand_int]
    i = low
    array[rand_int], array[high] = array[high], array[rand_int]
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


def main():
    array = [99, -2, 53, 4, 67, 55, 23, 43, 88, -22, 36, 45]
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('\nTotal taken time: {:.5f}'.format(time.time() - start_time))
