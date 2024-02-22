from typing import List


def counting_sort(array: List[int]) -> List[int]:
    """
    Counting sort.
    :param array:
    :return:
    """
    n = len(array)
    min_el = min(array)
    max_el = max(array)
    if min_el > 0 and max_el > 0:
        bookkeeping_array = [0] * (max_el - min_el + 1)
        for i in range(n):
            bookkeeping_array[array[i] - min_el] += 1
        k = 0
        m = len(bookkeeping_array)
        for i in range(m):
            for j in range(bookkeeping_array[i]):
                array[k] = min_el + i
                k += 1
        return array
    else:
        raise Exception("Every element in the array must "
                        "be an integer between 0...c")


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(counting_sort(array))
