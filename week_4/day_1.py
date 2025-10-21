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

print(output)
