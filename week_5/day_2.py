# OBJECT ORIENTED PROGRAMMING (OOP):
# OOP is a programming paradigm where we create a blueprint called a class,
# and use that class to create objects (instances).

# FUNCTIONAL PROGRAMMING:
# Focuses on using functions to perform computation without modifying data.

# PROCEDURAL PROGRAMMING:
# Organizes code into procedures (functions) that perform tasks step-by-step.

# MEASURE STRUCTURE:
# ATTRIBUTE: Attributes are the qualities or characteristics of an object.
# METHODS: Methods are the actions (functions) defined in a class that perform specific tasks.
# Example: speaking(), moving()

# TYPES OF ATTRIBUTES:
# 1. CLASS ATTRIBUTE – shared among all instances of the class.
# 2. INSTANCE ATTRIBUTE – unique to each instance.

# ---------------------------------------------------------------------

# Example 1: Simple Class Definition
class Person:  # Blueprint
    pass


# Creating objects (instances)
Miracle = Person()
Clinton = Person()
Tivsue = Person()
Cosmas = Person()


# ---------------------------------------------------------------------

# Example 2: Class with Attributes and Methods
class Footballer:
    # ---- Class Attributes ----
    game = "football"
    ball = "sphere"

    # ---- Instance Attributes ----
    def __init__(self, name, age, role):  # constructor
        self.name = name
        self.age = age
        self.role = role

    # ---- Method ----
    def information(self):
        return f"{self.name} plays {Footballer.game}. The ball is {Footballer.ball}."


# Creating objects (instances)
zinedine_zidane = Footballer("Zinedine Zidane", 34, "Attacking Midfielder")
cristiano_ronaldo = Footballer("Cristiano Ronaldo", 39, "Striker")

# Displaying their information
print(zinedine_zidane.information())
print(cristiano_ronaldo.information())
