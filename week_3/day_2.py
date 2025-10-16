# LOOP  is a block of code that keeps on running till a condition is meet.

# Loops in Python are used to repeat actions efficiently.

# The main types are For loops (counting through items) and While loops (based on conditions).

# While Loop
# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# When the condition becomes false,
# the line immediately after the loop in the program is executed.

# NB: multiple line comment is used for block of codes for easy debugging.

"""
num = 0
while num < 10:
print(num)
num = num + 1
"""

# Infinite While Loop
# If we want a block of code to execute infinite number of times
# then we can use the while loop in Python to do so.

"""
while (True):
print("Hello World!")
"""

#     For Loop
# For loops is used to iterate over a sequence such as a list, tuple, string or range.
# It allow to execute a block of code repeatedly, once for each item in the sequence.
# The break statement in Python brings control out of the loop.

"""
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]

for person in people:
    print(person)
    
searched_name = input("Who are you looking for")
for person in people:
    if person == searched_name:
        print(f"Person found: {person}")
        break # Stops the loop
else: #Runs the loop has stopped
    print("The person is not found.")
"""

# Classwork

"""
first_num = [1, 2, 3, 4, 5]
second_num = [6, 7, 8, 9, 10]

answer : [1,2,3,4,5,6,7,8,9,10]
hint use append()

for num in second_num:
    first_num.append(num)

print(first_num)
"""

# Next  task

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
updated = []
for num in numbers:
    num = num * 2
    updated.append(num)
else:
    print("Numbers:", numbers)
    print("Updated Numbers:", updated)
"""

# Next task

"""
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
email_users = []

for person in people:
    email_address = person + "@mail.com"
    email_users.append(email_address)
else:
    print(email_users)
"""

# Next
"""
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
name = input("Who do you want to delete: ")
for person in people:
    if person == name:
        people.remove(person)
        print(f"{person} Deleted.")
        break
else:
    print("The person is not found.")
"""

# Using strip for white spaces
"""
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
name = input("Who do you want to delete: ").strip()
for person in people:
    if person == name:
        people.remove(person)
        print(f"{person} Deleted.")
        break
else:
    print("The person is not found.")
"""

# small  and capital letters letter

people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
name = input("Who do you want to delete: ").strip()
for person in people:
    if name.lower() == person.lower():
        people.remove(person)
        print(f"{person} Deleted.")
        break
else:
    print("The person is not found.")
