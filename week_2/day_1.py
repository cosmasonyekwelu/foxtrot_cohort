# ------- Comparison Operators - Is use for comparing values or data

'''
 == Is Equal
 != Not Equal
 > Greater than 
 < Less than
 >= Greater than and Equal to
 <= Less than and Equal to
'''


stored_value = 10
search_input = 4

# Is equal
is_equal = stored_value == search_input
# print("Is Equal:", is_equal)

# Not Equal to
not_equal = stored_value != search_input
# print("Not Equal to:", not_equal)

# Greater than
greater_than = stored_value > search_input
# print("Greater than:", greater_than)

# Less than
less_than = stored_value < search_input
# print("Less than:", less_than)

# Greater than and equal to
greater_than_and_equal_to = stored_value >= search_input
# print("Greater than and equals to:", greater_than_and_equal_to)

# Less than and equal to
less_than_and_equal_to = stored_value <= search_input
# print("Less than and equal to:", less_than_and_equal_to)


# ----- Logical Operators - Are used to make more than one comparisons
"""
 AND - Checks if both comparisons are true
 OR - Check of one of them are true
 NOT - (Negation operator: Makes a value the opposite)
"""
age = 20
nysc = "done"

# AND OPERATOR
is_all_true = age >= 20 and nysc == "done"
# print("AND:", is_all_true)

# OR OPERATOR
is_one_true = age >= 20 or nysc == "in_transit"
# print("OR:", is_one_true)

# NOT OPERATOR - gives the opposite value
value = False
negate_value = not value
# print("NOT",negate_value)



# ----- STRINGS ------
# Any character or characters within a quote

# single quote string - a single line
# double quote string - a single line
# triple single quote - multi line  
# triple doubel quote - mutli line 

single_quote = 'I am in a single quote'

double_quote = "I am in a double quote"

triple_single_quote = ''' 
This is a triple single quote.
It is also multi line
'''

triple_double_quote = """
This is a triple multi quote
It works on multiple lines as well.
"""

'''
CHARACTERS THAT HAS FUNCTIONALITIES IN A STRING:
\n - new line character
\t - tab character
\\ - Backslash
\b - Erases a character
'''

sentence = '\tIt was a rainy\b day today and a lot of people. \\just using a backslash here. got stuck from coming to work.\nThere was also a heavy traffic.'

# Concatenation
str_1 = "A string"
str_2 = "is joined"
concat = str_1 + " " + str_2

# Interpolation - Passing in a value into a string through a placeholder
# f-string
name = "Miracle"
sent_1 = f"My name is {name}" # f-string for passing values inside string

# Repitition
repeat = name * 3

# Membership
is_a_member = "Book" in sent_1

# Some methods we use in a string.
replace_sentence =  "My name is Miracle".replace("Miracle", "Clinton") # replace

strip_sentence = " My name is Miracle ".strip() # Strip

to_upper = "My name is Miracle".upper()
to_lower = "My name is Miracle".lower()







