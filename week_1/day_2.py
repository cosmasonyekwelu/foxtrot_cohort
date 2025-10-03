# This is a single line comment used for documentation.

'''
This is a multi-line comment
   that spans multiple lines
    and is often used for documentation.
'''

# Variables and Data Types
bottle = "water"

# data types

"qwerty1234567890@#$%^&*()_+"  # string

1234567890  # integer

123.4567890  # float

True  # boolean
False  # boolean

first_name = "Cosmas"  # snake case

world = "Hello World!"  # string variable

print(world)  # print function to display output

# Arithmetic Operator
'''
+  Addition(Datatype - Integer, Floats, String)
-  Subtraction(Datatype - Integer, Floats, String)
*  Multiplication(Datatype - Integer, Floats)
 /  Division(Datatype - Integer, Floats)
 // Floor Division(for rounding down values) (Datatype - Integer, Floats)
'''

addition = 12 + 12  # Addition

concatenation = "Hello" + " " + "Cosmas"  # String Concatenation

repetition = "Hurray" * 3  # String Repetition

first_number = 4
second_number = 6

# Addition
add = first_number + second_number

# Subtraction
subtract = first_number - second_number

# Multiplication
multiply = first_number * second_number

# Division
divide = first_number / second_number


print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:", divide)

print("Addition:", add, "Type:", type(add))
print("Subtraction:", subtract, "Type:", type(subtract))
print("Multiplication:", multiply, "Type:", type(multiply))
print("Division:", divide, "Type:", type(divide))


# Casting - Changing one data type to another data type

'''
int() - convert to integer(string, float)-provided the fact that the characters are numbers
str() - convert to string(integer, boolean, float)
float() - convert to float (integer, string)-provided the fact that the characters are numbers
bool() - boolean("string")

'''

# converting addition to a string
convert_to_string = str(add)
print("Converting addition to string:",
      convert_to_string, type(convert_to_string))

# converting subtraction to a float
convert_to_float = float(subtract)
print("Converting subtraction to float:",
      convert_to_float, type(convert_to_float))

# converting multiplication to a boolean
convert_to_boolean = bool(multiply)
print("Converting multiplication to boolean:",
      convert_to_boolean, type(convert_to_boolean))

# converting divide to an integer
convert_to_int = int(divide)
print("Converting divide to integer:",
      convert_to_int, type(convert_to_int))

# Re-assigning a variable
nationality = "United States Of America"
nationality = "Nigerian"
nationality = "France"
print(nationality)

introduction = "Hello, My name is " + " " + \
    first_name + " I am from " + " " + nationality
print(introduction)
