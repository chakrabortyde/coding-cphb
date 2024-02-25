from typing import List, Any, Callable


def comparison_functions(array: List[Any], func: Callable) -> List[Any]:
    """

    :param array:
    :param func:
    :return:
    """
    array.sort(key=func)
    return array


if __name__ == "__main__":
    class User:
        def __init__(self, id: int, first_name: str, last_name: str):
            self.id = id
            self.first_name = first_name
            self.last_name = last_name

        def __repr__(self):
            return f"{self.id}: \"{self.first_name} {self.last_name}\""

    def compare(user: User):
        return user.id, user.last_name, user.first_name

    array = [
        User(3, "D", "B"),
        User(3, "E", "A"),
        User(2, "C", "C"),
        User(1, "A", "E"),
        User(1, "B", "D")
    ]
    print(comparison_functions(array, compare))
