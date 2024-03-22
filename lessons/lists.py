"""Demonstrate basic list syntax"""

#Initialize an empty list...lines 4 and 5 do the same thing, only need one of them 
grocery_list: list[str] = list() # list constructor
grocery_list: list[str] = [] #literal 

print(grocery_list)

#add item to a list
grocery_list.append("bananas")
grocery_list.append("bread")
grocery_list.append("milk")

print("After appending: ")
print(grocery_list)

#create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list: ")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

#indexing
print("Print first element of string")
print(grocery_list[0])

#modifying by index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change: ")
print(grocery_list)

#you can have duplicates
grocery_list.append("almond milk")
print(grocery_list)

#removing an item
grocery_list.pop(1)
print("After removing almond milk: ")
print(grocery_list)

# Function name: display
# Parameter: list[str]
#return nothing
#print list
print("Functions!")

def display(word: list[str]) -> None:
    print(word)

display(grocery_list)
x = display(["Alyssa", "Erin", "AK"])
print(x) #prints None bc nothing is returned with this function, if x is the result of calling function, it will be None 

#Create a list
#Name: create
#parameters: str and str 
#RV: list[str]
#Put both parameters into list and return that list 

def create(x: str, y: str) ->list[str]:
    my_list: list[str] = [x, y]
    return my_list
print(create("hello", "hi"))

def average(numbers: list[int]) -> float:
    total = 0.0
    for elem in numbers:
        total += elem
    return total / len(numbers)



a: list[int] = [0,1,2,3,4]
print(average(a))

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for item in list2:
    list1.append(item)

print(list1)

for i in range(5):
    result = i * 2
print(result)
