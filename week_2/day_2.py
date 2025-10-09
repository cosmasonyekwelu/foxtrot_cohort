# Data Structures in Python.
# Data structures are used to store multiple values in a single variable.
# There are four built-in data structures in Python: List, Tuple, Set, Dictionary.

'''
dictionary
list
tuple
set
'''
# Dictionary
person = {
    "first_name": "Justice",
    "last_name": "Rivers",
    "age": 28,
    "gender": "Male",
    "profession": "Pet Engineer", "tags": ["a, ab"],
    "nationality": {
        "nation": "Nigeria",
        "nin": 3456789023,
        "tax": "all paid in full"
    }
}
# print(type(person))
'''
print(
    person["age"]
)

'''
introduction = f"Hello {person["first_name"]} {person["last_name"]} from {person["nationality"]["nation"]}. It's nice to meet You"
# print(introduction)

# Update or Reassign values in keys
person["profession"] = "Software Engineer"

# Assign new key with a value in a dictionary
person["club"] = "Liverpool"

# Delete a key
del person["gender"]

# searches if the firstname is in the dictionary
get_first_name = person.get("first_name")
# searches if the firstname is in the dictionary, If not return the value Adams
get_first_name_or_return = person.get("first_name", "Adam")

# person.pop("age", "Age not found")  # removes a key with its value

# person.clear()  # Removes the entire key  with its dictionary

# print(person)

# List
datas = ["paul", 22, False, 14.5, person, [1, 2, 3, 4, 5]]
# print(type(datas))
'''
print(
    datas[4]["nationality"]["nin"]
)
'''
datas[0] = "John"

del datas[5]

# print(datas)

concat = [1, 2, 3, 4, 5] + [6, 7, 8, 9, 0]  # Concatenation

is_in_datas = 48 in datas  # Membership

daniel_bryan = ["Yes"] * 4  # Repetition
# print(daniel_bryan)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers.append(11)  # Add at the end
numbers.insert(5, 100)  # Add a data to a particular index
numbers.pop(6)  # Removes items from the list through index
numbers.remove(0)  # Removes items from the list through values
# print(numbers)

# Simple Classwork

nested_number = [2, 46, 33, 1, 6, 3, ["twenty", "Yes", 5,
                                      6, {"another": [3, 55, 6, "middle", 17]}, 7], 55, 2, 4]
# Locate yes
# print(nested_number[6][1])

# Add "end" to the list of another
# nested_number[6][4]["another"].append("end")
# print(nested_number)

# Delete the number 7
# nested_number[6].remove(7)
# print(nested_number)

# or

# del nested_number[6][5]
# print(nested_number)

# Tuples
colors = ("red", "blue", "yellow", "red")  # Immutable
# print(colors)

# colors[0] ="Orange" will not work because it is immutable

repeat = colors * 2
# print(repeat)

membership = "blue" in colors
# print(membership)

concat_tuple = colors + ("orange", "green", "purple")
# print(concat_tuple)

color_count = colors.count("red")
# print(color_count)

# del colors[0] will not work because it is immutable
# print(colors[3])

# Sets is a collection of unordered items
# In Python, sets are mutable, un-indexed and do not contain duplicates.
# The order of elements in a set is not preserved and can change.

top_4_clubs = {"Arsenal", "Liverpool", "Tottenham", "Bouremouth"}
# print(top_4_clubs)
regulars = {"Fullham", "Bouremouth", "Burnley", "Wolves"}
# print(regulars)

# top_4_clubs.clear() # Clear values out of sets

# common value between set (short cut &)
intersect = top_4_clubs.intersection(regulars)
# print(intersect)
union = top_4_clubs.union(regulars)  # join sets (short cut |)
# print(union)

# Not common values between sets (short cut -)
difference = top_4_clubs.difference(regulars)
print(difference)
