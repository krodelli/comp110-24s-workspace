def odd_and_even(numbers: list[int]) -> list [int]:
    new_list: list[int] = []
    idx: int = 0
    while idx < len(numbers):
        if numbers[idx] % 2 == 1 and idx % 2 == 0:
            new_list.append(numbers[idx])
        idx += 1 
    return new_list

a: list[int] = [2, 3, 4, 5]
b: list[int] = [7, 8, 10, 10, 5, 12, 3 ,2, 11]

def short_words(words: list[str]) -> list[str]:
    new_list: list[str] = []
    idx: int = 0
    while idx < len(words):
        if len(words[idx]) < 5:
            new_list.append(words[idx])
        else:
            print(f"{words[idx]} is too long!")
        idx += 1 
    return new_list


def short_words(inp_list: list[str]) -> list[str]:
        """Filter out the shorter words"""
        ret_list: list[str] = []
        for x in inp_list:
            if len(x) < 5:
                ret_list.append(x)
            else:
                print(f"{x} is too long!")
        return ret_list

a: list[str] = ["hello", "gooood", "hi", "hel"]
print(short_words(a))