from functools import total_ordering
from typing import List, Any


def user_defined_structs(array: List[Any]) -> List[Any]:
    """

    :param array:
    :return:
    """
    array.sort()
    return array


if __name__ == "__main__":
    @total_ordering
    class UserStruct:
        def __init__(self, id: int, first_name: str, last_name: str):
            self.id = id
            self.first_name = first_name
            self.last_name = last_name

        def __lt__(self, other):
            return (
                self.id, self.last_name.lower(), self.first_name.lower()) < (
                other.id, other.last_name.lower(), other.first_name.lower())

        def __eq__(self, other):
            return (
                self.id, self.last_name.lower(), self.first_name.lower()) == (
                other.id, other.last_name.lower(), other.first_name.lower())

        def __gt__(self, other):
            return (
                self.id, self.last_name.lower(), self.first_name.lower()) > (
                other.id, other.last_name.lower(), other.first_name.lower())

        def __repr__(self):
            return f"{self.id}: \"{self.first_name} {self.last_name}\""


    array = [
        UserStruct(3, "D", "B"),
        UserStruct(3, "E", "A"),
        UserStruct(2, "C", "C"),
        UserStruct(1, "A", "E"),
        UserStruct(1, "B", "D")
    ]
    print(user_defined_structs(array))
