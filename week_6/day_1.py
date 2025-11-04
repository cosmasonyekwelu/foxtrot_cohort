# Composition
# meaning : is building complex objects by combining simpler ones.

class A:
    def __init__(self):
        self.name = "This is class A"
        
class B:
    def __init__(self):
        self.name = "This is class B"
        self.a = A()  # B has an instance of A
        
b = B()
print(b.name)        # Output: This is class B
print(b.a.name)     # Output: This is class A