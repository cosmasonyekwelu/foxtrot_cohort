# Comparison Operators in Python
# Comparison operators are used to compare two data or values.

'''
== Is Equal
!= Not Equal
> Greater Than
<  Less Than
>= Greater Than and Equal To
<= Less Than and Equal To
'''

stored_value = 10
search_input = 4
# Is Equal
is_equal = stored_value == search_input
print("Is Equal: ", is_equal)

# Not Equal
not_equal = stored_value != search_input
print("Not Equal to: ", not_equal)

# Greater Than
greater_than = stored_value > search_input
print("Greater Than: ", greater_than)

# Less Than
less_than = stored_value < search_input
print("Less Than: ", less_than)

# Greater Than and Equal To
greater_than_and_equal_to = stored_value >= search_input
print("Greater Than and Equal To: ", greater_than_and_equal_to)

# Less Than and Equal To
less_than_and_equal_to = stored_value <= search_input
print("Less Than and Equal To: ", less_than_and_equal_to)


# -------Logical Operators in Python-------
''''
 Logical operators are used to make more than one comparison.
There are three logical operators in Python: AND, OR, NOT.
AND - Operator-checks if both the comparisons are true.
OR - Operator-checks if at least one of the comparisons is true.
NOT - Operator-reverses the result of the comparison.(Negative operator: makes a value the opposite)
'''
age = 20
nyse = "done"
# AND Operator
is_all_true = age >= 20 and nyse == "done"
print("AND: ", is_all_true)

# OR Operator
is_one_true = age >= 20 or nyse == "in_transit"
print("OR: ", is_one_true)

# NOT Operator : gives the opposite value
is_not_true = not(age >= 20 and nyse == "done")
print("NOT: ", is_not_true)

value = False
negate_value = not value
print("Not: ", negate_value)