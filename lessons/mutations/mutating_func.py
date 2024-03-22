"""Mutate vs not"""

def remove_first(input_list: list[str]) -> None:
    input_list.pop(0)


def get_first(input_list: list[str]) -> str:
    return input_list[0]


def get_and_remove_first(input_list: list[str]) -> str:
    elem: str = input_list[0]
    input_list.pop(0)
    return elem 
