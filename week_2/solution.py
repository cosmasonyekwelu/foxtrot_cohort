# ====================== PYTHON BEGINNER CLASSWORK ======================

# 1. Write 3 examples using comparison operators (==, !=, >, <, >=, <=).
#    Print the result for each one.


# No 1 answer here
x = 2
y = 4

# Example 1
compare_1 = x == y

# Example 2
compare_2 = x > y

# Example 2
compare_3 = x <= y


# 2. Create two variables: stored_value = 12 and search_input = 12.
#    Check if they are equal and print the result.

# No 2 answer here
stored_value = 12
search_input = 12

is_equal = stored_value == search_input
print(is_equal)


# 3. Use comparison operators to check:
#    - if 5 is greater than 10
#    - if 15 is less than or equal to 20
#    Print both results.


# No 3 answer here
is_greater = 5 > 10
is_less_than_or_equal_to = 10 < 20
print(is_greater)
print(is_less_than_or_equal_to)


# 4. Use logical operators to check:
#    - if a person's age is greater than or equal to 18 AND if they have a driver's license.
#    Example:
#    age = 20
#    license = "yes"
#    Print the result of the comparison.

# No 4 answer here
age = 20
license = "yes"

is_drivers_licence = age >= 18 and license
print(is_drivers_licence)


# 5. Use OR (||) to check if one of these is true:
#    temperature = 35
#    raining = False
#    Check if temperature > 30 or raining == True
#    Print the result.

# No 5 answer here
temperature = 35
raining = False

is_one_true = temperature > 30 or raining
print(is_one_true)

# 6. Use NOT to flip the value of a variable:
#    Example:
#    is_tired = False
#    Use NOT to make it True and print both values.

# No 6 answer here
is_tired = False
negate = not is_tired


# 7. Create 4 string variables:
#    - One using single quotes
#    - One using double quotes
#    - One using triple single quotes
#    - One using triple double quotes
#    Print all of them.

# No 7 answer here
str1 = 'single quote'
str2 = "double quote"
str3 = ''' triple singe quote'''
str4 = """triple double quote"""
print(str1, str2, str3, str4)


# 8. Write a sentence that uses \n for a new line and \t for a tab space.
#    Print it and see how it looks.

# No 8 answer here
letter = "Hello Sir,\n\tI want to express my gratitude."
print(letter)

# 9. Use string methods:
#    - Make a string called name = " miracle "
#    - Remove spaces using .strip()
#    - Change it to uppercase using .upper()
#    - Change it to lowercase using .lower()
#    - Print each result.


# No 9 answer here
name = " miracle "
remove_spaces = name.strip()
to_upper = name.upper()
to_lower = name.lower()

print(name)
print(remove_spaces)
print(to_upper)
print(to_lower)

# 10. Do the following with strings:
#     - Concatenate two strings, for example: "Python" + " Programming"
#     - Use an f-string to print your name inside a sentence (Example: f"My name is {name}")
#     - Use * (multiplication) to repeat a word 3 times.
#     - Print all results.


# No 10 answer here
str5 = "Hello"
str6 = "World"

concat = str5 + " " + str6
interpolation = f"My first text word in programming is {str5} {str6}"
repitition = str5 * 3
print(concat)
print(interpolation)
print(repitition)
