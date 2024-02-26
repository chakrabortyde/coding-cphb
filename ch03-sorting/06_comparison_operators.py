from typing import List


def comparison_operators(array: List[tuple]) -> List[tuple]:
    """

    :param array:
    :return:
    """
    array.sort(key=lambda x: (x[0], x[1]))
    return array


if __name__ == "__main__":
    array = [(9, 10), (7, 8), (5, 6), (3, 4), (1, 2)]
    print(comparison_operators(array))
