# Sets in Python

fruits = {"apple", "banana", "mango", "apple"}       # Creating a set
print("Fruits Set:", fruits)   # Duplicate "apple" ek hi baar aayega

numbers = set([1, 2, 3, 4, 2, 3])          # Using set() constructor
print("Numbers Set:", numbers)

fruits.add("orange")                    # Adding elements
print("After adding:", fruits)

fruits.update(["grapes", "cherry"])            # Updating multiple elements
print("After update:", fruits)

fruits.remove("banana")  # Removing elements
print("After remove:", fruits)

fruits.discard("apple")   # Error nahi dega agar element missing ho
print("After discard:", fruits)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}                 # Set operations

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)
print("Symmetric Difference:", A ^ B)

for item in fruits:                       # Looping through a set
    print("Fruit:", item)
