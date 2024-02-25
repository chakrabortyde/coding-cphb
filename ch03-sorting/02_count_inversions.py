from typing import List


def count_inversions(array: List[int]) -> (int, List[tuple]):
    """
    Count inversions.
    :param array:
    :return:
    """
    n = len(array)
    inversions = []
    for a in range(n - 1):
        for b in range(a + 1, n):
            if a < b and array[a] > array[b]:
                inversions.append((array[a], array[b]))
    return len(inversions), inversions


if __name__ == "__main__":
    array = [1, 2, 2, 6, 3, 5, 9, 8]
    count, inversions = count_inversions(array)
    print(f"The array has {count} inversions: {inversions}")
