from typing import List


def inbuilt_sort_with_comparison(array: List[tuple]) -> List[tuple]:
    """

    :param array:
    :return:
    """
    array.sort(key=lambda x: (x[0], x[1]))
    return array


if __name__ == "__main__":
    array = [(9, 10), (7, 8), (5, 6), (3, 4), (1, 2)]
    print(inbuilt_sort_with_comparison(array))
