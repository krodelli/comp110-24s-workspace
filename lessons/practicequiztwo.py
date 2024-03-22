def even_and_three(numbers: list[int]) -> str:
    string: str = ""
    for elem in range(0, len(numbers)):
       if numbers[elem] % 2 == 0 or numbers[elem] % 3 == 0:
            string += str(numbers[elem])
    return string   
    
    
    
    
    

boooool: list[bool] = [1==2, 5>2]

def average(nums: list[int]) -> int:
    """Averages"""
    total: int = 0
    for num in nums:
        total += num
    return total // len(nums)

a: list[int] = [1,2,3,4,5]




b: list[int] = [1,2,3]
new: list[int] = []
for elem in a:
    b.append(elem)

    
nums = [1,2,3,4,5]
for n in nums:
    n = n * 2


def odd_or_even(nums: list[int], oddeven: str) -> str:
    string: str = ""
    if oddeven == "even":
        for elem in nums:
            if elem % 2 == 0:
                string += str(elem)
    elif oddeven == "odd":
        for elem in nums:
            if elem % 2 == 1:
                string+=str(elem)
    return string

a: list[1,2,3,4,5]
x = "odd"
b: list[int] = list()
for idx in range (1,len(a)):
    b.append(a[idx])
print(b)
    