import json

# x = '{"name": "Alice", "age": 30, "city": "New York"}'


# to_dict = json.loads(x)


# open ("store.txt", "r")

# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file ex

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

x = {"name": "Alice", "age": 30, "city": "New York"}

# with open("store.json", "w") as store:
#     convert_to_json = json.dumps(x)
#     store.write(convert_to_json)

# Read
# with open("store.json") as f:
#     content = json.loads(f.read())
#     print(type(content))


# types of methods

class Main:
    def unique(self):
        pass

    @classmethod
    def generic(cls):
        pass

    @staticmethod
    def utility():
        pass
