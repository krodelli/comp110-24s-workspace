word: str = "Computerscience"
index: int = 0

while index < len(word):
    string: str = word[index]
    if index % 2 == 1:
        print(string)
    index += 1 



