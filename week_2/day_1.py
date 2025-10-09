# Comparison Operators in Python.
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
is_not_true = not (age >= 20 and nyse == "done")
print("NOT: ", is_not_true)

value = False
negate_value = not value
print("Not: ", negate_value)

# Strings
# A string is any character or characters  within a single quote or double quotes.
# single_quote_string = 'Hello, World!' : a single line
# double_quote_string = "Hello, World!" : a single line
# triple_quote_string : a multi-line
# triple_double_quote_string : a multi-line

single_quote = 'I am in a single quote'
double_quote = "I am in a double quote"
triple_quote = '''I am in a triple quote
I can be multi-line'''
triple_double_quote = """I am in a triple double quote
I can also be multi-line"""

''''
CHARACTERS THAT HAS FUNCTIONALITIES IN  A STRING
\n : New Line Character
\t : Tab Character
\\ : Backslash Character
\b : Erase a Character
\' : Single Quote Character
\" : Double Quote Character
'''

sentence = '\tit was a rainy\b day today and a lot of people \\just using the backslash here, got stuck from coming to work \n There was also a heavy traffic'
print(sentence)

# Concatination of Strings
str_1 = "A string"
str_2 = "is joined"
concat = str_1 + " " + str_2
print("Concatenated String: ", concat)

# Interpolation of Strings- passing in a value into a string through a placeholder
# f-strings are used to embed expressions inside string literals, using curly braces {}.
name = "Cosmas"
sent_1 = f"My name is {name}"
print("F-string: ", sent_1)

# Repetition of Strings
repeat = name * 3

# Membership
is_a_member = "Book" in sent_1
print("Is a member: ", is_a_member)

# Some methods we use in string.
replace_word = sent_1.replace("Cosmas", "John")


replace_sentence = "My name is John".replace("John", "Doe")  # Replace

strip_sentence = "My name is John ".strip()  # Strip

to_lower = "My name is John".lower()  # Lower Case
to_upper = "My name is John".upper()  # Upper Case
print(to_lower)

# title_case = "my name is john".title()  # Title Case
# find_substring = "My name is John".find("John")  # Find Substring
# split_string = "My name is John".split()  # Split String into a list
