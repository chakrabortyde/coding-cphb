from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """
    Merge sort.
    :param array:
    :return:
    """
    n = len(array)
    if n > 1:
        k = n // 2
        subarray_one = merge_sort(array[:k])
        subarray_two = merge_sort(array[k:])

        i, j, k = 0, 0, 0
        m, n = len(subarray_one), len(subarray_two)
        while i < m and j < n:
            if subarray_one[i] < subarray_two[j]:
                array[k] = subarray_one[i]
                i += 1
            else:
                array[k] = subarray_two[j]
                j += 1
            k += 1
        while i < m:
            array[k] = subarray_one[i]
            i += 1
            k += 1
        while j < n:
            array[k] = subarray_two[j]
            j += 1
            k += 1
    return array


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(merge_sort(array))
