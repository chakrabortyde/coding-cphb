from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """
    Bubble sort.
    :param array:
    :return:
    """
    n = len(array)
    for i in range(n):
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(array))
