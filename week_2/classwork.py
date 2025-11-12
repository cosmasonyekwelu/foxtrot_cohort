# ====================== PYTHON BEGINNER CLASSWORK ======================

# 1. Write 3 examples using comparison operators (==, !=, >, <, >=, <=).
#    Print the result for each one.


# No 1 answer here

# 2. Create two variables: stored_value = 12 and search_input = 12.
#    Check if they are equal and print the result.


# No 2 answer here
stored_value = 12
search_input = 12
is_equal= stored_value == search_input
print("Is Equal :", is_equal)


# 3. Use comparison operators to check:
#    - if 5 is greater than 10
#    - if 15 is less than or equal to 20
#    Print both results.



# No 3 answer here
greater_than = 5 > 10 
print(greater_than)

lesser_than = 15 <= 20
print(lesser_than)


# 4. Use logical operators to check:
#    - if a person's age is greater than or equal to 18 AND if they have a driver's license.
#    Example:
#    age = 20
#    license = "yes"
#    Print the result of the comparison.


# No 4 answer here

age = 20
license = "yes"
is_all_true = age >= 18 and license == "yes"
print("AND:", is_all_true)


# 5. Use OR (||) to check if one of these is true:
#    temperature = 35
#    raining = False
#    Check if temperature > 30 or raining == True
#    Print the result.

# No 5 answer here
temperature = 35
raining = False
is_one_true = temperature > 30 or raining == True
print("or: " ,is_one_true)

# 6. Use NOT to flip the value of a variable:
#    Example:
#    is_tired = False
#    Use NOT to make it True and print both values.

# No 6 answer here
is_tired = False
not_tired = not is_tired
print("not: ", not_tired)

# 7. Create 4 string variables:
#    - One using single quotes
#    - One using double quotes
#    - One using triple single quotes
#    - One using triple double quotes
#    Print all of them.

# No 7 answer here
'Clinton is king'
"clinton is king"
'''
clinton is king
clinton is king
'''
"""
clinton is king
clinton is king
"""


# 8. Write a sentence that uses \n for a new line and \t for a tab space.
#    Print it and see how it looks.

# No 8 answer here
gift = "My name is Gift \nClinton"
print(gift)

slim = "That girl is quite slim and jovial  \t"
# 9. Use string methods:
#    - Make a string called name = " miracle "
#    - Remove spaces using .strip()
#    - Change it to uppercase using .upper()
#    - Change it to lowercase using .lower()
#    - Print each result.


# No 9 answer here
name = "Miracle"
to_strip = "Miracle".strip()
print(to_strip)
to_upper = "Miracle".upper()
print(to_upper)
to_lower = "Miracle".lower()
print(to_lower)

# 10. Do the following with strings:
#     - Concatenate two strings, for example: "Python" + " Programming"
#     - Use an f-string to print your name inside a sentence (Example: f"My name is {name}")
#     - Use * (multiplication) to repeat a word 3 times.
#     - Print all results.


# No 10 answer here
str_1 = "Python"
str_2 = " Programming"
concat = print(str_1 + " " + str_2)
name = 'Clinton'
print(f"My name is {name}")

repeat = name * 3
print(name)