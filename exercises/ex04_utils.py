"""List utility functions."""

__author__ = "730466512"

# part 1 all function 


def all(numbers: list[int], number: int) -> bool:
    """Returns True if all numbers match indicated number."""
    if len(numbers) == 0:
        return False
    index: int = 0
    while index < len(numbers):
        if numbers[index] != number:
            return False
        index += 1
    return True
        

# max function defining part 2 
        

def max(input: list[int]) -> int:
    """Returns highest number in list."""
    if len(input) == 0:  # value error if empty list. 
        raise ValueError("max() arg is an empty List")
    max_value = input[0]  # initalizes max value. 
    index_max: int = 0
    while index_max < len(input):
        if input[index_max] > max_value:
            max_value = input[index_max]
        index_max += 1 
    return max_value 

# part 3 is equal 


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    if len(list_one) != len(list_two):
        return False
    
    i: int = 0
    while i < len(list_one):
        if list_one[i] != list_two[i]:
            return False
        i += 1
    return True 


# part 4 extend 


def extend(list_one: list[int], list_two: list[int]) -> None:
    """Mutating one of the inputs by adding the second lists values to the firsts."""
    i: int = 0  # initialize the index variable for list two. 
    while i < len(list_two):  # iterate until the end of list two. 
        list_one.append(list_two[i])  # add index i of list two to list one. 
        i += 1 