# ----- DATA STRUCTURES ------ 

'''
dictionary
list
tuple
set
'''

# Dictionary
person = {
    "first_name": "Justice",
    "last_name":  "Rivers",
    "age": 28,
    "gender": "Male",
    "profession": "Petroleum Engineer",
    "nationality": {
        "nation": "Nigeria",
        "nin": 3454575632425,
         "tax": "im a free man"
    },
    "tags": ["a", "sd"]
}

# print(type(person))

introduction  = f"Hello {person["first_name"]} {person["last_name"]} from {person["nationality"]["nation"]}. It's nice to meet you."

# Update or reassign values in keys.
person["profession"] = "Software Engineer"

#Assign new key with a value in a dictionary
person["club"] = "Liverpool"

# Deletes a key with it's value
del person["gender"]

get_first_name = person.get("first_name", "Adams") # Searches if first_name is in the dictionary, if not return the value Adams.

 # removes a key with it's value

# person.clear() # removes the entire key with it's dictionary

# str = "This is string"

# List
datas = ["Paul", 22, False, 14.5, person, [1,2,3,4,5]]
# print(type(datas))


datas[0] = "John" # Assigning value into an existing list

del datas[5] # deleting data inside a list

concat = [1,2,3,4,5] + [6,7,8,9,0] # Concatenation

is_in_datas = 48 in datas # Membership

daniel_bryan = ["Yes"] * 4 # Repitition


numbers = [1,2,3,4,5,6,7,8,9,0, "end"]

numbers.append(11) # adds at the end

numbers.insert(5, 100) # Add a data at a particular index

numbers.pop(3) # Removes items from the list through the index

numbers.remove(0) # Removes items from the list through the value


# Simple classwork
nested_numbers = [2, 46, 33, 1, 6, 3,["twenty", "yes", 5, 6, {"another": [3, 55, 6, "middle", 17]},7], 55, 2, 4]

# Locate yes
# add "end" to the list of another
# delete the number 7

# print(
#     nested_numbers[6][1]
# )

nested_numbers[6][4]['another'].append("end")

del nested_numbers[6][5]


# Tuple

colors = ("red", 'blue', "yellow", "red") # Immutable

# colors[0] = "orange" # This does not work because it is immutable

repeat = colors * 2
membership = "blue" in colors
concat = colors + ("orange", "green", "purple")

c = colors.count("red")

# del colors[0] # This does not work because it is immutable


# Set
top_4 = {"Arsenal", "Liverpool", "Tottenham", "Bournemouth"}

regulars = {"Fulham", "Bournemouth", "Burnley", "Wolves"}

#top_4.clear() # Clear values out of set
# Check for other methods to use as well.

intersect = top_4.intersection(regulars) # Common value between two sets # Short from for intersection -> top_4 & regulars
union = top_4.union(regulars) # Joins sets # short form for union -> top_4 | regulars
difference = top_4.difference(regulars) # Not common values between sets # short form for difference -> top_4 - regulars

print(difference)







