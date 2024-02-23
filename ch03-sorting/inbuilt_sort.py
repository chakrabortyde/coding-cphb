from typing import List


def inbuilt_sort(array: List[int]) -> List[int]:
    """

    :param array:
    :return:
    """
    array.sort()
    return array


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(inbuilt_sort(array))
