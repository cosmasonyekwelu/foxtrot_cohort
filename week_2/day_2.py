# Data Structures in Python
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
    "profession": "Pet Engineer",
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
print(introduction)

# Update or Reassign values in keys
person["profession"] = "Software Engineer"

# Assign new key with a value in a dictionary
person["club"] = "Liverpool"

# Delete a key
del person["gender"]

print(person)
