x: str = "Hello"
y: int = len(x)
if y % 4 ==1:
    y*=2
y-=6
print(y)
print(x[y])
print(type(y))
print(type(x[y]))