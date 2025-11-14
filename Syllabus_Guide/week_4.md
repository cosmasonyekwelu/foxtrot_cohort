# Object-Oriented Programming (OOP) in Python - Comprehensive Guide

## Module 1: Introduction to Object Oriented Programming (OOP)

### What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. An object is a data field that has unique attributes and behavior.

### Core Principles of OOP

**1. Encapsulation**

- Bundling of data with the methods that operate on that data
- Restricting direct access to some of an object's components

**2. Inheritance**

- Mechanism where one class acquires the properties and behaviors of another class
- Promotes code reusability

**3. Polymorphism**

- Ability of an object to take on many forms
- Same interface for different underlying forms

**4. Abstraction**

- Hiding complex implementation details and showing only essential features

### Why Use OOP?

```python
# Procedural vs Object-Oriented approach example

# Procedural approach
def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

length = 5
width = 3
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

# Object-Oriented approach
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Usage
rect = Rectangle(5, 3)
area = rect.calculate_area()
perimeter = rect.calculate_perimeter()
```

### Benefits of OOP

- **Modularity**: Objects can be maintained separately
- **Reusability**: Classes can be reused across programs
- **Scalability**: Easy to maintain and modify existing code
- **Security**: Data hiding and encapsulation protect data

## Module 2: Classes & Objects in Python

### Understanding Classes and Objects

**Class**: A blueprint for creating objects. It defines the attributes and methods that the objects will have.

**Object**: An instance of a class. It contains actual data and can perform actions.

```python
# Basic class definition
class Car:
    """A simple Car class"""

    # Class attribute (shared by all instances)
    vehicle_type = "automobile"

    def __init__(self, brand, model, year):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    # Instance method
    def accelerate(self, increment):
        """Increase the car's speed"""
        self.speed += increment
        return f"{self.brand} {self.model} is now going {self.speed} km/h"

    def brake(self, decrement):
        """Decrease the car's speed"""
        self.speed = max(0, self.speed - decrement)
        return f"{self.brand} {self.model} slowed down to {self.speed} km/h"

    def get_info(self):
        """Return car information"""
        return f"{self.year} {self.brand} {self.model}"

# Creating objects (instances)
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

# Accessing attributes and methods
print(car1.get_info())  # Output: 2022 Toyota Camry
print(car2.accelerate(30))  # Output: Honda Civic is now going 30 km/h

# Accessing class attribute
print(f"Vehicle type: {Car.vehicle_type}")  # Output: Vehicle type: automobile
print(f"Car1 type: {car1.vehicle_type}")    # Output: Car1 type: automobile
```

### The `self` Parameter

- `self` refers to the current instance of the class
- It's used to access variables and methods associated with the current object
- It must be the first parameter of any instance method

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # self.name is instance attribute
        self.age = age    # self.age is instance attribute

    def display_info(self):
        # self allows access to instance attributes
        return f"Student: {self.name}, Age: {self.age}"

# Creating instances
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.display_info())  # Output: Student: Alice, Age: 20
print(student2.display_info())  # Output: Student: Bob, Age: 22
```

## Module 3: Constructors in Python

### Understanding Constructors

A constructor is a special method that is automatically called when an object of a class is created. In Python, the `__init__` method serves as the constructor.

### The `__init__` Method

```python
class Person:
    # Class constructor
    def __init__(self, name, age, city):
        print("Constructor called! Creating a new Person object.")
        self.name = name
        self.age = age
        self.city = city
        self.created_at = "2024"  # Default value

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old from {self.city}"

# Creating objects triggers the constructor
person1 = Person("John", 25, "New York")
# Output: Constructor called! Creating a new Person object.

print(person1.introduce())  # Output: Hi, I'm John, 25 years old from New York
```

### Constructor with Default Parameters

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0, account_type="Savings"):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_type = account_type
        self.account_number = self._generate_account_number()

    def _generate_account_number(self):
        """Private method to generate account number"""
        import random
        return f"ACC{random.randint(10000, 99999)}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds"

# Creating accounts with different parameters
account1 = BankAccount("Alice")  # Uses default balance and type
account2 = BankAccount("Bob", 1000)  # Uses default type
account3 = BankAccount("Charlie", 5000, "Checking")  # All parameters provided

print(account1.deposit(200))  # Output: Deposited $200. New balance: $200
print(account2.withdraw(300)) # Output: Withdrew $300. New balance: $700
```

### Multiple Constructors (Using Class Methods)

```python
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    @classmethod
    def from_string(cls, employee_string):
        """Alternative constructor from string"""
        name, salary, department = employee_string.split(',')
        return cls(name, float(salary), department)

    @classmethod
    def create_intern(cls, name):
        """Alternative constructor for interns"""
        return cls(name, 0, "Intern")

    def display_info(self):
        return f"{self.name} - {self.department} - ${self.salary}"

# Different ways to create Employee objects
emp1 = Employee("John Doe", 50000, "Engineering")
emp2 = Employee.from_string("Jane Smith,60000,Marketing")
emp3 = Employee.create_intern("Mike Johnson")

print(emp1.display_info())  # Output: John Doe - Engineering - $50000
print(emp2.display_info())  # Output: Jane Smith - Marketing - $60000
print(emp3.display_info())  # Output: Mike Johnson - Intern - $0
```

## Module 4: Class and Instance Attributes

### Understanding Attribute Types

**Instance Attributes**: Belong to specific instances of a class. Each object has its own copy.

**Class Attributes**: Belong to the class itself. Shared by all instances.

```python
class Company:
    # Class attributes
    company_name = "TechCorp"
    location = "San Francisco"
    employee_count = 0  # Shared across all instances

    def __init__(self, department, manager):
        # Instance attributes
        self.department = department
        self.manager = manager
        self.employees = []  # Each instance has its own list

        # Modifying class attribute
        Company.employee_count += 1
        self.employee_id = Company.employee_count

    def hire_employee(self, name, position):
        employee = {
            'id': len(self.employees) + 1,
            'name': name,
            'position': position,
            'department': self.department
        }
        self.employees.append(employee)
        return f"Hired {name} as {position} in {self.department}"

    def get_department_info(self):
        return f"{self.department} Department (Manager: {self.manager})"

    @classmethod
    def get_company_info(cls):
        return f"{cls.company_name} - {cls.location} - Total Employees: {cls.employee_count}"

# Creating instances
dept1 = Company("Engineering", "Alice Johnson")
dept2 = Company("Marketing", "Bob Smith")

# Using instance methods and attributes
print(dept1.get_department_info())  # Output: Engineering Department (Manager: Alice Johnson)
print(dept1.hire_employee("Charlie", "Software Engineer"))

# Accessing class attributes
print(Company.get_company_info())  # Output: TechCorp - San Francisco - Total Employees: 2
print(dept1.company_name)          # Output: TechCorp (accessed through instance)

# Modifying class attribute affects all instances
Company.company_name = "TechCorp Global"
print(dept2.company_name)  # Output: TechCorp Global
```

### Attribute Access and Namespace

```python
class Example:
    class_var = "I am a class variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var

obj = Example("I am an instance variable")

# Accessing attributes
print(obj.instance_var)    # Instance attribute
print(obj.class_var)       # Class attribute (through instance)
print(Example.class_var)   # Class attribute (through class)

# Attribute lookup order: instance -> class -> parent classes
```

## Module 5: Adding Attributes to a Python Class

### Different Ways to Add Attributes

```python
class SmartPhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._battery_level = 100  # Protected attribute
        self.__serial_number = self._generate_serial()  # Private attribute

    def _generate_serial(self):
        """Generate a serial number"""
        import uuid
        return str(uuid.uuid4())[:8]

    def add_feature(self, feature_name, feature_value):
        """Dynamically add features to the phone"""
        feature_name = feature_name.lower().replace(' ', '_')
        setattr(self, feature_name, feature_value)
        return f"Added feature: {feature_name} = {feature_value}"

    def remove_feature(self, feature_name):
        """Dynamically remove features"""
        if hasattr(self, feature_name):
            delattr(self, feature_name)
            return f"Removed feature: {feature_name}"
        else:
            return f"Feature {feature_name} not found"

    def get_private_info(self):
        """Access private attribute through method"""
        return f"Serial: {self.__serial_number}"

    def set_battery(self, level):
        """Setter method with validation"""
        if 0 <= level <= 100:
            self._battery_level = level
            return f"Battery level set to {level}%"
        else:
            return "Invalid battery level"

# Creating smartphone instance
phone = SmartPhone("Apple", "iPhone 15")

# Adding attributes dynamically
phone.add_feature("storage", "256GB")
phone.add_feature("camera_mp", 48)
phone.add_feature("water_resistant", True)

# Accessing attributes
print(f"Brand: {phone.brand}")
print(f"Storage: {phone.storage}")
print(f"Camera: {phone.camera_mp}MP")
print(phone.get_private_info())

# Removing attributes
print(phone.remove_feature("storage"))
print(phone.remove_feature("nonexistent_feature"))

# Using property-like methods
print(phone.set_battery(85))
```

### Using Properties for Controlled Attribute Access

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property for fahrenheit"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit"""
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        """Computed property for kelvin"""
        return self._celsius + 273.15

# Using properties
temp = Temperature(25)
print(f"Celsius: {temp.celsius}")      # Output: Celsius: 25
print(f"Fahrenheit: {temp.fahrenheit}") # Output: Fahrenheit: 77.0
print(f"Kelvin: {temp.kelvin}")        # Output: Kelvin: 298.15

# Using setters
temp.celsius = 30
print(f"New Fahrenheit: {temp.fahrenheit}") # Output: New Fahrenheit: 86.0

temp.fahrenheit = 100
print(f"New Celsius: {temp.celsius}") # Output: New Celsius: 37.777...
```

## Module 6: Adding Methods to a Python Class

### Types of Methods in Python Classes

```python
class Calculator:
    # Class attribute
    operation_count = 0

    def __init__(self, name="Default Calculator"):
        self.name = name
        self.memory = 0
        self.history = []

    # Instance method - operates on instance data
    def add(self, a, b):
        result = a + b
        self._record_operation(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self._record_operation(f"{a} - {b} = {result}")
        return result

    # Protected method (convention: single underscore)
    def _record_operation(self, operation):
        """Record operation in history"""
        self.history.append(operation)
        Calculator.operation_count += 1
        if len(self.history) > 10:  # Keep only last 10 operations
            self.history.pop(0)

    # Private method (name mangling: double underscore)
    def __reset_memory(self):
        """Private method to reset memory"""
        self.memory = 0
        return "Memory reset"

    # Public method that uses private method
    def clear_all(self):
        self.history.clear()
        return self.__reset_memory()

    # Class method - operates on class data
    @classmethod
    def get_operation_count(cls):
        return f"Total operations performed: {cls.operation_count}"

    @classmethod
    def create_scientific_calc(cls):
        """Alternative constructor"""
        calc = cls("Scientific Calculator")
        calc.memory = 100  # Extra memory for scientific calc
        return calc

    # Static method - doesn't need class or instance data
    @staticmethod
    def about():
        return "This is a calculator class for basic arithmetic operations"

    # Special methods (magic/dunder methods)
    def __str__(self):
        return f"Calculator: {self.name} (Memory: {self.memory})"

    def __repr__(self):
        return f"Calculator('{self.name}')"

    def __len__(self):
        return len(self.history)

# Using the calculator
calc1 = Calculator("Basic Calc")
calc2 = Calculator.create_scientific_calc()

# Instance methods
print(calc1.add(5, 3))        # Output: 8
print(calc1.subtract(10, 4))  # Output: 6

# Class method
print(Calculator.get_operation_count())  # Output: Total operations performed: 2

# Static method
print(Calculator.about())  # Output: This is a calculator class...

# Special methods
print(str(calc1))   # Output: Calculator: Basic Calc (Memory: 0)
print(len(calc1))   # Output: 2 (number of operations in history)

# Accessing history (instance attribute)
print("History:", calc1.history)
```

### Method Chaining

```python
class StringBuilder:
    def __init__(self, initial_string=""):
        self.string = initial_string

    def append(self, text):
        self.string += str(text)
        return self  # Return self for method chaining

    def prepend(self, text):
        self.string = str(text) + self.string
        return self

    def insert(self, text, position):
        if 0 <= position <= len(self.string):
            self.string = self.string[:position] + str(text) + self.string[position:]
        return self

    def clear(self):
        self.string = ""
        return self

    def build(self):
        return self.string

    def __str__(self):
        return self.string

# Method chaining example
result = (StringBuilder("Hello")
          .append(" World")
          .prepend(">>> ")
          .insert(" Beautiful", 6)
          .build())

print(result)  # Output: >>> Hello Beautiful World
```

## Module 7: Deleting Attributes and Objects

### Deleting Attributes and Objects in Python

```python
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        self.courses = []
        self.gpa = 0.0

    def enroll_course(self, course_name):
        self.courses.append(course_name)
        return f"Enrolled in {course_name}"

    def drop_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            return f"Dropped {course_name}"
        return f"Not enrolled in {course_name}"

    def calculate_gpa(self, grades):
        if grades:
            self.gpa = sum(grades) / len(grades)
        return self.gpa

    def __del__(self):
        print(f"Student object {self.name} is being destroyed")

# Creating student objects
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 21, "Mathematics")

# Adding attributes dynamically
student1.scholarship = True
student1.dormitory = "North Hall"

print("Before deletion:")
print(f"student1 attributes: {student1.__dict__}")

# Deleting attributes using del
del student1.dormitory
print(f"After deleting dormitory: {student1.__dict__}")

# Deleting attributes using delattr()
delattr(student1, 'scholarship')
print(f"After deleting scholarship: {student1.__dict__}")

# Checking attribute existence
print(f"Has age attribute: {hasattr(student1, 'age')}")  # Output: True
print(f"Has scholarship attribute: {hasattr(student1, 'scholarship')}")  # Output: False

# Deleting entire objects
print("Deleting student2...")
del student2  # This triggers __del__ method

# Garbage collection demonstration
import gc

class MemoryHeavy:
    def __init__(self, size):
        self.data = [0] * size  # Large list to consume memory

    def __del__(self):
        print(f"MemoryHeavy object with {len(self.data)} elements destroyed")

# Creating and deleting large objects
print("Creating large objects...")
obj1 = MemoryHeavy(1000000)
obj2 = MemoryHeavy(500000)

print("Deleting objects...")
del obj1
del obj2

# Force garbage collection to see __del__ being called
print("Forcing garbage collection...")
gc.collect()
```

### Using `__del__` for Cleanup

```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w')
        print(f"File {filename} opened")

    def write_data(self, data):
        self.file.write(data + '\n')
        return f"Data written to {self.filename}"

    def close_file(self):
        if self.file and not self.file.closed:
            self.file.close()
            print(f"File {self.filename} closed properly")

    def __del__(self):
        # Destructor - called when object is garbage collected
        self.close_file()

# Using FileHandler
handler = FileHandler("example.txt")
handler.write_data("Hello, World!")
handler.write_data("This is a test.")

# When handler goes out of scope or is deleted, __del__ is called
print("End of scope - __del__ will be called automatically")
```

## Module 8: Inheritance in OOP

### Understanding Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

```python
# Base class (Parent class)
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model} engine started"

    def stop_engine(self):
        self.is_running = False
        self.speed = 0
        return f"{self.brand} {self.model} engine stopped"

    def accelerate(self, increment):
        if self.is_running:
            self.speed += increment
            return f"Accelerating to {self.speed} km/h"
        return "Start the engine first"

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, doors, fuel_type):
        # Call parent class constructor
        super().__init__(brand, model, year)
        # Add car-specific attributes
        self.doors = doors
        self.fuel_type = fuel_type
        self.trunk_open = False

    # Car-specific methods
    def open_trunk(self):
        self.trunk_open = True
        return "Trunk opened"

    def close_trunk(self):
        self.trunk_open = False
        return "Trunk closed"

    # Override parent method
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - {self.doors} doors, {self.fuel_type}"

# Another child class
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc, has_sidecar):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc
        self.has_sidecar = has_sidecar
        self.kickstand_down = True

    def raise_kickstand(self):
        self.kickstand_down = False
        return "Kickstand raised"

    def lower_kickstand(self):
        self.kickstand_down = True
        return "Kickstand lowered"

    # Override start_engine with additional logic
    def start_engine(self):
        if self.kickstand_down:
            return "Cannot start engine with kickstand down"
        return super().start_engine()

# Using the classes
car = Car("Toyota", "Camry", 2023, 4, "Gasoline")
bike = Motorcycle("Harley", "Davidson", 2022, 1200, False)

print(car.start_engine())  # Inherited method
print(car.accelerate(30))  # Inherited method
print(car.open_trunk())    # Car-specific method
print(car.get_info())      # Overridden method

print(bike.raise_kickstand())
print(bike.start_engine())  # Overridden method with additional logic
```

### Multiple Inheritance

```python
class Engine:
    def __init__(self, horsepower, cylinders):
        self.horsepower = horsepower
        self.cylinders = cylinders
        self.engine_on = False

    def start(self):
        self.engine_on = True
        return "Engine started"

    def stop(self):
        self.engine_on = False
        return "Engine stopped"

class ElectricMotor:
    def __init__(self, battery_capacity, voltage):
        self.battery_capacity = battery_capacity
        self.voltage = voltage
        self.motor_on = False

    def start(self):
        self.motor_on = True
        return "Electric motor started"

    def stop(self):
        self.motor_on = False
        return "Electric motor stopped"

# Hybrid vehicle inheriting from multiple classes
class HybridCar(Vehicle, Engine, ElectricMotor):
    def __init__(self, brand, model, year, horsepower, battery_capacity):
        # Initialize Vehicle
        Vehicle.__init__(self, brand, model, year)
        # Initialize Engine
        Engine.__init__(self, horsepower, 4)
        # Initialize ElectricMotor
        ElectricMotor.__init__(self, battery_capacity, 400)

        self.mode = "electric"  # electric, gas, hybrid

    def switch_mode(self, new_mode):
        if new_mode in ["electric", "gas", "hybrid"]:
            self.mode = new_mode
            return f"Switched to {new_mode} mode"
        return "Invalid mode"

    def start_engine(self):
        if self.mode == "electric":
            return ElectricMotor.start(self)
        elif self.mode == "gas":
            return Engine.start(self)
        else:  # hybrid
            ElectricMotor.start(self)
            Engine.start(self)
            return "Both engines started"

# Using hybrid car
hybrid = HybridCar("Toyota", "Prius", 2023, 120, 50)
print(hybrid.start_engine())
print(hybrid.switch_mode("electric"))
```

## Module 9: Method Overriding in Python

### Understanding Method Overriding

Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def move(self):
        return f"{self.name} is moving"

    def sleep(self):
        return f"{self.name} is sleeping"

    def __str__(self):
        return f"{self.species} named {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    # Overriding make_sound method
    def make_sound(self):
        return "Woof! Woof!"

    # Adding new method specific to Dog
    def fetch(self, item):
        return f"{self.name} is fetching the {item}"

    # Overriding __str__ method
    def __str__(self):
        return f"{self.breed} dog named {self.name}"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    # Overriding make_sound method
    def make_sound(self):
        return "Meow!"

    # Overriding move method with different behavior
    def move(self):
        return f"{self.name} is gracefully walking"

    # Adding cat-specific method
    def climb_tree(self):
        return f"{self.name} is climbing a tree"

class Bird(Animal):
    def __init__(self, name, species, can_fly=True):
        super().__init__(name, species)
        self.can_fly = can_fly
        self.wingspan = 0

    # Overriding move method
    def move(self):
        if self.can_fly:
            return f"{self.name} is flying"
        else:
            return f"{self.name} is walking or hopping"

    # Adding bird-specific method
    def set_wingspan(self, wingspan):
        self.wingspan = wingspan
        return f"Wingspan set to {wingspan} cm"

# Testing method overriding
animals = [
    Dog("Buddy", "Golden Retriever"),
    Cat("Whiskers", "Tabby"),
    Bird("Tweety", "Canary"),
    Bird("Ostrich", "Ostrich", False)
]

for animal in animals:
    print(f"{animal}: {animal.make_sound()} - {animal.move()}")
    print("-" * 50)
```

### Using `super()` in Overridden Methods

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

    def calculate_bonus(self):
        return self.salary * 0.10  # 10% bonus

class Manager(Employee):
    def __init__(self, name, salary, department, team_size):
        # Call parent constructor using super()
        super().__init__(name, salary)
        self.department = department
        self.team_size = team_size

    # Override get_details but extend functionality
    def get_details(self):
        # Get base details from parent
        base_details = super().get_details()
        # Add manager-specific details
        return f"{base_details}, Department: {self.department}, Team Size: {self.team_size}"

    # Override calculate_bonus with different calculation
    def calculate_bonus(self):
        # Base bonus from parent class
        base_bonus = super().calculate_bonus()
        # Additional bonus for management
        management_bonus = self.salary * 0.05  # Extra 5%
        team_bonus = self.team_size * 100      # $100 per team member
        return base_bonus + management_bonus + team_bonus

class Executive(Manager):
    def __init__(self, name, salary, department, team_size, stock_options):
        super().__init__(name, salary, department, team_size)
        self.stock_options = stock_options

    # Override calculate_bonus further
    def calculate_bonus(self):
        # Get bonus from Manager class
        manager_bonus = super().calculate_bonus()
        # Add executive bonus
        executive_bonus = self.stock_options * 0.01  # 1% of stock options
        return manager_bonus + executive_bonus

# Testing the hierarchy
emp = Employee("John", 50000)
mgr = Manager("Alice", 80000, "Engineering", 8)
exec = Executive("Bob", 120000, "Technology", 15, 50000)

print(emp.get_details())
print(f"Bonus: ${emp.calculate_bonus():.2f}\n")

print(mgr.get_details())
print(f"Bonus: ${mgr.calculate_bonus():.2f}\n")

print(exec.get_details())
print(f"Bonus: ${exec.calculate_bonus():.2f}")
```

## Module 10: Polymorphism and Abstraction

### Polymorphism in Python

Polymorphism allows methods to do different things based on the object that is acting upon them.

```python
from math import pi

# Polymorphism with inheritance
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return self.__class__.__name__

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Polymorphism in action
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 4, 6, 5, 5)
]

for shape in shapes:
    print(f"{shape}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
```

### Abstraction in Python

Abstraction focuses on hiding the complex implementation details and showing only the essential features.

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class PaymentMethod(ABC):
    def __init__(self, amount):
        self.amount = amount
        self.transaction_id = None

    @abstractmethod
    def process_payment(self):
        """Process the payment - must be implemented by subclasses"""
        pass

    @abstractmethod
    def refund(self):
        """Process refund - must be implemented by subclasses"""
        pass

    def get_transaction_details(self):
        return f"Amount: ${self.amount}, Transaction ID: {self.transaction_id}"

class CreditCardPayment(PaymentMethod):
    def __init__(self, amount, card_number, expiry_date, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self):
        # Simulate payment processing
        import random
        self.transaction_id = f"CC{random.randint(100000, 999999)}"
        return f"Credit card payment processed. Transaction ID: {self.transaction_id}"

    def refund(self):
        if self.transaction_id:
            return f"Refund processed for transaction {self.transaction_id}"
        return "No transaction to refund"

class PayPalPayment(PaymentMethod):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process_payment(self):
        # Simulate PayPal payment processing
        import random
        self.transaction_id = f"PP{random.randint(100000, 999999)}"
        return f"PayPal payment processed for {self.email}. Transaction ID: {self.transaction_id}"

    def refund(self):
        if self.transaction_id:
            return f"PayPal refund initiated for {self.email}"
        return "No transaction to refund"

class BankTransferPayment(PaymentMethod):
    def __init__(self, amount, account_number, routing_number):
        super().__init__(amount)
        self.account_number = account_number
        self.routing_number = routing_number

    def process_payment(self):
        # Simulate bank transfer
        import random
        self.transaction_id = f"BT{random.randint(100000, 999999)}"
        return f"Bank transfer initiated. Transaction ID: {self.transaction_id}"

    def refund(self):
        return "Bank transfers cannot be refunded automatically. Please contact support."

# Using abstraction - client code doesn't need to know implementation details
payments = [
    CreditCardPayment(100, "1234-5678-9012-3456", "12/25", "123"),
    PayPalPayment(75, "user@example.com"),
    BankTransferPayment(200, "987654321", "021000021")
]

for payment in payments:
    print(payment.process_payment())
    print(payment.get_transaction_details())
    print(payment.refund())
    print("-" * 50)
```

### Duck Typing (Python's Approach to Polymorphism)

```python
# Duck typing: "If it looks like a duck and quacks like a duck, it must be a duck"
class TextFile:
    def read(self):
        return "Reading data from text file"

    def write(self, data):
        return f"Writing '{data}' to text file"

class Database:
    def read(self):
        return "Fetching data from database"

    def write(self, data):
        return f"Storing '{data}' in database"

class API:
    def read(self):
        return "Making GET request to API"

    def write(self, data):
        return f"Making POST request with data: {data}"

# Function that works with any object that has read() and write() methods
def data_processor(data_source, data_to_write=None):
    print(data_source.read())

    if data_to_write:
        print(data_source.write(data_to_write))

# Using duck typing - all these work because they have the required methods
sources = [
    TextFile(),
    Database(),
    API()
]

for source in sources:
    data_processor(source, "Hello World")
    print("=" * 40)
```

## Module 11: Operator Overloading

### Understanding Operator Overloading

Operator overloading allows you to define how operators behave with user-defined objects.

```python
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    # Arithmetic operators
    def __add__(self, other):
        """Overload + operator"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        """Overload - operator"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __mul__(self, other):
        """Overload * operator (dot product or scalar multiplication)"""
        if isinstance(other, (int, float)):
            # Scalar multiplication
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            # Dot product
            return self.x * other.x + self.y * other.y + self.z * other.z
        return NotImplemented

    def __rmul__(self, other):
        """Overload right multiplication (scalar * vector)"""
        if isinstance(other, (int, float)):
            return self * other  # Call __mul__
        return NotImplemented

    # Comparison operators
    def __eq__(self, other):
        """Overload == operator"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __lt__(self, other):
        """Overload < operator (compare magnitude)"""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        return NotImplemented

    # Other useful methods
    def magnitude(self):
        """Calculate vector magnitude"""
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def normalize(self):
        """Return normalized vector"""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0, 0)
        return Vector(self.x/mag, self.y/mag, self.z/mag)

    # Container-like behavior
    def __getitem__(self, index):
        """Overload indexing v[0], v[1], v[2]"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Vector index out of range")

    def __len__(self):
        """Overload len() function"""
        return 3  # Vectors always have 3 components

    # Callable object
    def __call__(self, scalar):
        """Make vector callable for scaling"""
        return self * scalar

# Testing operator overloading
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Vector 1:", v1)
print("Vector 2:", v2)

# Arithmetic operations
print("v1 + v2 =", v1 + v2)
print("v2 - v1 =", v2 - v1)
print("v1 * 2 =", v1 * 2)
print("3 * v1 =", 3 * v1)  # Uses __rmul__
print("Dot product v1 * v2 =", v1 * v2)

# Comparison operations
print("v1 == v2?", v1 == v2)
print("v1 < v2?", v1 < v2)

# Other operations
print("Magnitude of v1:", v1.magnitude())
print("Normalized v1:", v1.normalize())
print("v1[0] =", v1[0])
print("Length of vector:", len(v1))
print("v1 scaled by 2.5:", v1(2.5))  # Using __call__
```

### Complete Example: Complex Numbers with Operator Overloading

```python
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imaginary})"

    # Arithmetic operators
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imaginary)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imaginary * other.imaginary
            imaginary = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(real, imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imaginary * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real**2 + other.imaginary**2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            return ComplexNumber(real, imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real / other, self.imaginary / other)
        return NotImplemented

    # Right-hand operations
    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return ComplexNumber(other, 0) - self

    def __rmul__(self, other):
        return self * other

    # Comparison operators
    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        elif isinstance(other, (int, float)):
            return self.real == other and self.imaginary == 0
        return False

    # Additional methods
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def modulus(self):
        return (self.real**2 + self.imaginary**2) ** 0.5

    def argument(self):
        import math
        return math.atan2(self.imaginary, self.real)

# Testing complex number operations
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -2)

print("c1 =", c1)
print("c2 =", c2)

print("c1 + c2 =", c1 + c2)
print("c1 - c2 =", c1 - c2)
print("c1 * c2 =", c1 * c2)
print("c1 / c2 =", c1 / c2)
print("c1 + 5 =", c1 + 5)
print("10 * c1 =", 10 * c1)

print("Conjugate of c1:", c1.conjugate())
print("Modulus of c1:", c1.modulus())
print("Argument of c1:", c1.argument())

print("c1 == ComplexNumber(3, 4)?", c1 == ComplexNumber(3, 4))
print("c1 == 3?", c1 == 3)
```

### Common Magic Methods for Operator Overloading

```python
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # String representations
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages}, {self.price})"

    # Comparison operators
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and
                   self.author == other.author and
                   self.pages == other.pages)
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Book):
            return self.pages <= other.pages
        return NotImplemented

    # Arithmetic operators (for price calculations)
    def __add__(self, other):
        if isinstance(other, Book):
            return self.price + other.price
        elif isinstance(other, (int, float)):
            return self.price + other
        return NotImplemented

    def __radd__(self, other):
        return self + other

    # Boolean evaluation
    def __bool__(self):
        return len(self.title) > 0 and self.pages > 0

    # Length (number of pages)
    def __len__(self):
        return self.pages

# Using the Book class
book1 = Book("Python Programming", "John Doe", 350, 29.99)
book2 = Book("Data Science", "Jane Smith", 450, 39.99)

print(book1)           # Uses __str__
print(repr(book1))     # Uses __repr__

print("book1 == book2?", book1 == book2)
print("book1 < book2?", book1 < book2)

print("Total price:", book1 + book2)
print("Book1 + 10:", book1 + 10)

print("Boolean value:", bool(book1))
print("Number of pages:", len(book1))
```

This comprehensive OOP course covers all fundamental concepts with practical examples, providing a solid foundation in object-oriented programming with Python. Each concept builds upon the previous ones, creating a complete understanding of how to design and implement object-oriented systems.
