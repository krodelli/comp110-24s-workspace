def remove_first_even(words: list[str]) -> None:
        idx: int = 0
        condition: bool = True
        while (idx < len(words)) and condition:
            if len(words[idx]) % 2 == 0:
                words.pop(idx)
                condition = False
            idx += 1

def value_exists(input_dict: dict[str, int], input_num: int) -> bool:
    for key in input_dict:
        if input_dict[key] == input_num:
            return True
    else: 
        return False
         

def plus_or_minus(inp: dict[str, int], n: int) -> None:
     """Mutates."""
     for key in inp:
        if inp[key] % 2 == 1:
            inp[key] -= n
        if inp[key] % 2 == 0:
            inp[key] += n


diction: dict[str,int] = {"a": 2, "b": 4, "c": 7}
test_val: int = 2
result = plus_or_minus(diction, test_val)
print(diction)

