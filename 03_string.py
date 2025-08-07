# Python Strings

name = "Sualiah Naim"

# Basic Operations
print("Original:", name)
print("Stripped:", name.strip()) # Remove starting and end spaces
print("Lowercase:", name.lower())
print("Uppercase:", name.upper())
print("Replace:", name.replace("Naim", "Akhtar"))
print("Length:", len(name))
print("String ends with:", name.endswith("am"))
print("Counting word:", name.count("a"))

# Indexing and Slicing
print("First character:", name[0])
print("Slice [2:8]:", name[2:8])

# String Formatting
age = 20
print(f"My name is {name.strip()} and I am {age} years old.")
