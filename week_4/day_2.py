from my_module import my_addition_function
from functools import reduce
# Higher Order Functions
# Higher Order Functions are functions that take a function as an argument, or return a function as its result.
# This is possible because functions in Python are first-class objects, meaning:
# You can assign them to variables,
# Pass them as arguments,
# Return them from other functions,
# Store them in data structures (like lists or dictionaries


def speak():
    return "Ola. Nice to meet You"


def man(name, func):
    return f"{name}:{func()}"


call = man("Jerry", speak)

# print(call)

# map(), filter(), and reduce() are three of Python’s most useful higher-order functions.

# map(function, iterable)
# map() applies a function to every item in an iterable (like a list) and
# returns a map object (which you can convert to a list).
# It’s used when you want to transform data, not filter or combine it.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def multiply_by_two(item):
# print(item)
# return item * 2


# map_func = map(multiply_by_two, numbers)

# print(list(map_func))

# print(my_addition_function(5, 10))

# filter(function, iterable) :Return a new filtered list
# filter() function is used to extract elements from an iterable
# (like a list, tuple or set) that satisfy a given condition.
# It works by applying a function to each element and keeping only those for which function returns True.
# What it does:
# filter() filters (selects) elements from an iterable based on a condition (True/False).
# It keeps only the elements for which the function returns True.


def no_remainder(item):
    # print(item)
    return item % 2 == 0


filter_func = filter(no_remainder, numbers)
# print(list(filter_func))

# reduce(function, iterable, initial_value) Return a reduced value of the iterable
# What it does:
# reduce() applies a rolling computation on items in a sequence
# it reduces the iterable to a single cumulative value.
# Unlike map() and filter(), it’s not a built-in function
# you have to import it from functools. # from functools import reduce


# def concatenate(param_one, param_two):
#     print(param_one, param_two)
#     return param_one + param_two


# reduce_func = reduce(concatenate, numbers)
# print(reduce_func)

sentence = ["A", "stitch", "in", "time", "saves", "nine"]


def concatenate(param_one, param_two):
    print(param_one, param_two)
    return param_one + " " + param_two


reduce_func = reduce(concatenate, sentence)
print(reduce_func)

# Lambda Functions are anonymous functions means that the function is without a name.
# As we already know def keyword is used to define a normal function in Python.
# Similarly, lambda keyword is used to define an anonymous function in Python.

filter_func = filter(lambda item: item % 2 == 0, numbers)
# print(list(filter_func))
def outer 

