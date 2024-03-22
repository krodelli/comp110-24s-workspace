"""Practice with dictionaries."""

#syntax for defining dictionary, can also use single quote in dictionaries instead of double for strings 
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

ice_cream["oreo"] = 12 # adding 

ice_cream.pop("oreo") # remove

print(ice_cream["vanilla"]) #accessing.. print how many ordered vanilla
print(f"Number of vanilla orders: {ice_cream['vanilla']}") # f string with accessing

#updating a value
ice_cream["vanilla"] += 1 
print(f"Number of vanilla orders: {ice_cream['vanilla']}") # f string with accessing

#length of dictionary 
len(ice_cream)

#check if key in dictionary, returns a boolean
print("oreo" in ice_cream)
"chocolate" in ice_cream

# cannot have multiple of the same key... memory issue. you can have duplicates of the same value 

print(ice_cream)

ice_cream2: dict[str, float] = {"chocolate": 12, "vanilla": 10, "strawberry": 5}
for key in ice_cream2:
    print(f"{key} has {ice_cream2[key]} orders.")