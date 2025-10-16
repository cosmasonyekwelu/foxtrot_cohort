# LOOP  is a block of code that keeps on running till a condition is meet.
# Loops in Python are used to repeat actions efficiently.
# The main types are For loops (counting through items) and While loops (based on conditions).
# While Loop
# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# When the condition becomes false,
# the line immediately after the loop in the program is executed.

num = 0
while num < 10:
    print(num)
    num = num + 1

# Infinite While Loop
# If we want a block of code to execute infinite number of times
# then we can use the while loop in Python to do so.
while (True):
    print("Hello World!")
