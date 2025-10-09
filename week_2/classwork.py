# ====================== PYTHON BEGINNER CLASSWORK =======================

# 1. Write 3 examples using comparison operators (==, !=, >, <, >=, <=).
#    Print the result for each one.

# No 1 answer here
value_one = 10
value_two = 5
value_three = 10
print(value_one == value_three)
print(value_three >= value_two)
print(value_one <= value_two)


# 2. Create two variables: stored_value = 12 and search_input = 12.
#    Check if they are equal and print the result.

# No 2 answer here
stored_value = 12
search_input = 12
check_result = stored_value == search_input
print(check_result)


# 3. Use comparison operators to check:
#    - if 5 is greater than 10
#    - if 15 is less than or equal to 20
#    Print both results.

# No 3 answer here
is_greater = 5 > 10
is_less_equal = 15 <= 20
print(is_greater)
print(is_less_equal)


# 4. Use logical operators to check:
#    - if a person's age is greater than or equal to 18 AND if they have a driver's license.
#    Example:
#    age = 20
#    license = "yes"
#    Print the result of the comparison.

# No 4 answer here
age = 24
driver_license = "yes"
valid_driver = age >= 18 and driver_license == "yes"
print(valid_driver)


# 5. Use OR (||) to check if one of these is true:
#    temperature = 35
#    raining = False
#    Check if temperature > 30 or raining == True
#    Print the result.

# No 5 answer here
temperature = 35
raining = False
weather_check = temperature > 30 or raining == True
print(weather_check)


# 6. Use NOT to flip the value of a variable:
#    Example:
#    is_tired = False
#    Use NOT to make it True and print both values.

# No 6 answer here
is_tired = False
did_no_work = is_tired
has_worked = not is_tired
print(did_no_work)
print(has_worked)


# 7. Create 4 string variables:
#    - One using single quotes
#    - One using double quotes
#    - One using triple single quotes
#    - One using triple double quotes
#    Print all of them.

# No 7 answer here
single = 'Single quotes Example'
double = "Double quotes Example"
triple_single = '''Triple single quotes
Example'''
triple_double = """Triple double quotes
Example"""
print(single)
print(double)
print(triple_single)
print(triple_double)


# 8. Write a sentence that uses \n for a new line and \t for a tab space.
#    Print it and see how it looks.

# No 8 answer here
print("Hello!\n My name is Cosmas. \tWelcome to Python Backend class.")


# 9. Use string methods:
#    - Make a string called name = " miracle "
#    - Remove spaces using .strip()
#    - Change it to uppercase using .upper()
#    - Change it to lowercase using .lower()
#    - Print each result.

# No 9 answer here
name = " miracle "
strip_name = name.strip()
upper_name = name.upper()
lower_name = name.lower()
print(strip_name)
print(upper_name)
print(lower_name)


# 10. Do the following with strings:
#     - Concatenate two strings, for example: "Python" + " Programming"
#     - Use an f-string to print your name inside a sentence (Example: f"My name is {name}")
#     - Use * (multiplication) to repeat a word 3 times.
#     - Print all results.

# No 10 answer here
text_one = "Python"
text_two = " Programming"
print(text_one + text_two)
my_name = "Cosmas"
print(f"My name is {my_name}")
School = "Univelcity"
print(School * 3)
