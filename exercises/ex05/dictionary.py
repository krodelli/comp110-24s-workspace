"""Dictionary."""

__author__ = "730466512"

# part 1 invert.


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    invert_dictionary: dict[str, str] = {}
    for key in dictionary:  # iterate through keys of input.
        value = dictionary[key]  # access value corresponding to key.
        if value in invert_dictionary:
            raise KeyError("Duplicate value when inverting dictionary!")
        invert_dictionary[value] = key 
    return invert_dictionary

# part 2 favorite color.


def favorite_color(name_color: dict[str, str]) -> str:
    """Return the most popular color."""
    color_count: dict[str, int] = {}  # initializing empty dictionary to keep track of how many times a color appears.
    for name in name_color:  
        color = name_color[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    most_common = ""  # initalizing empty string that will be returned.
    max_count = 0
    for color in color_count:  
        count = color_count[color]
        if count > max_count or (count == max_count and most_common == ""):
            most_common = color
            max_count = count
    return most_common

# part three count.


def count(words: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value in the list and each value is the number of times the value appeared."""
    dictionary: dict[str, int] = {}  # Initalize empty dictionary that we will add to. 
    for word in words:  # for each word in the string parameter, if the word is already in dictionary, add an integer to count. 
        if word in dictionary:
            dictionary[word] += 1 
        else:
            dictionary[word] = 1
    return dictionary 

# part four alphebetizer.


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Produce a dictionary where each key is a unique letter in alphabet and value is list of words that start with the letter."""
    dictionary: dict[str, list[str]] = {}  # initalize empty dictionary. 
    for word in words:
        first_letter = word[0].lower()  # make the first letter of the word lowercase.
        if first_letter not in dictionary:  # check if first letter is in the dictionary. 
            dictionary[first_letter] = [word]  # if not, create a new piece of the dictionary with the letter as the key. 
        else:
            dictionary[first_letter] += [word]
    return dictionary 

# part five update attendance.


def update_attendance(attendance: dict[str, list[str]], day_of_week: str, student: str) -> None:
    """Mutate and return the attendance dictionary."""
    if day_of_week in attendance:  # does the day of week exist in attendance?
        if student not in attendance[day_of_week]:
            attendance[day_of_week].append(student)  # if so, add it to the student information.
    else:
        attendance[day_of_week] = [student]  # if not, create new.