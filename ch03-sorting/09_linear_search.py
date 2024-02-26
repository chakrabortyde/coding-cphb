from typing import List


def linear_search(array: List[int], x: int) -> int:
    """

    :param x:
    :param array:
    :return:
    """
    for idx, a in enumerate(array):
        if a == x:
            return idx
    return -1


if __name__ == "__main__":
    array = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    print(linear_search(array, 1))
