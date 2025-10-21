# Functions
"""
Python Functions are a block of code that does a specific task. 
The idea is to put some commonly or repeatedly done task together and make a function 
so that instead of writing the same code again and again for different inputs,
we can do the function calls to reuse code contained in it over and over again.
1. Modularity: Organizes code into manageable sections.
2. Reusability: Increases code reusability.
3. Readability: Enhances code readability and maintainability.
"""


def addition():  # Function definition
    num_1 = 1  # The input to the function
    num_2 = 2
    sum = num_1 + num_2
    return sum  # The value you want to return

    num = 3  # Unreachable code after return statement


output = addition()  # Calling a function. This will return 3

# print(output)


def subtraction():
    return 2-1


output = subtraction()
# print(output)

"""
what function can return
string
boolean
integer
float
list 
tuple
dictionary
set 
function
variable
"""


def introduction():
    return "Hi my name is Cosmas"


# print(
#     introduction()
# )

age = 12  # Global Variable


def func():
    name = "Cosmas"  # Local Variable
    return "His Name is " + name + " and he is " + str(age)


# print(
#     func()
# )

# Parameters and Argument
# Function arguments are the values or variables passed into a function when it is called.
# The behavior of a function often depends on the arguments passed to it.
#  A Python function may be invoked from any other function by passing required data
# (called parameters or arguments).
#  The called function returns its result back to the calling environment.
# While defining a function, you specify a list of variables (known as formal parameters) within the parentheses.
# These parameters act as placeholders for the data that will be passed to the function when it is called.
# When the function is called, value to each of the formal arguments must be provided.
# Those are called actual arguments

def func_1(words):
    return words


print(
    func_1("This is an argument")
)


def reuseable_addition(num_one, num_two):
    return num_one + num_two


output_one = reuseable_addition(14, 2)
output_two = reuseable_addition(4, 4)
output_three = reuseable_addition(16, 18)
# print(output_one, output_two, output_three)

# Types of argument


def func_2(pos1, pos2, pos3):
    return pos1, pos2, pos3
# Positional or Required Arguments
# Required arguments are the arguments passed to a function in correct positional order.
# Here, the number of arguments in the function call should match exactly with the function definition,
# otherwise the code gives a syntax error.


func_2("first value", "second value", "Third Value")  # Positional argument

# Keyword Arguments
# Keyword arguments are related to the function calls. When you use keyword arguments in a function call,
# the caller identifies the arguments by the parameter name.
# This allows you to skip arguments or place them out of order
# because the Python interpreter is able to use the keywords provided to match the values with parameters.

func_2(pos1="first value", pos2="second value",
       pos3="third value")  # Keyword argument

# Default Arguments
# A default argument is an argument that assumes a default value
# if a value is not provided in the function call for that argument.


def game(mode="easy"):
    return f"Game on!!! mode {mode}"


print(
    game()
)

print(
    game("hard")
)

# ARGS or Variable-length Arguments
# You may need to process a function for more arguments than you specified while defining the function.
# These arguments are called variable-length arguments and are not named in the function definition
# , unlike required and default arguments.


def func_4(*param):
    return param # The structure is a turple


print(
    func_4("red", "blue", "yellow", "green")
)


# KWARGS - keyword as an argument
def func_5(**param):
    return param # A dictionary is returned


print(
    func_5(
        name="Miracle",
        email="miracle@mail.com",
        availability=True,
        rating=8.0
    )
)
