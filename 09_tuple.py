# Tuple in Python :Tuple is an immutable data type / structure in python

#  TUPLE METHODS
t1 = (10, 20, 30, 40)
t2 = ("apple", "banana", "cherry")

print("Tuple t1:", t1)
print("Tuple t2:", t2)

print("First element:", t1[0])  # Accessing elements
print("Last element:", t1[-1])

print("Slice 1:3 =", t1[1:3])    # Slicing

print("Count of 20:", t1.count(20))   # Counting
print("Index of 30:", t1.index(30))

t3 = t1 + t2               # Concatenation
print("Concatenated tuple:", t3)

a, b, c, d = t1              # Tuple unpacking
print("Unpacked values:", a, b, c, d)

print("Length of t1:", len(t1))   # Length of tuple

my_list = [1, 2, 3, 4]         # Convert list to tuple
new_tuple = tuple(my_list)
print("Converted from list:", new_tuple)

print("Is 20 in t1?:", 20 in t1)        # Check if item exists
print("Is 'orange' in t2?:", "orange" in t2)

print("Looping through t2:")            # Looping through tuple
for item in t2:
    print(item)

t4 = (1, "hello", [5, 6, 7], (8, 9))      # Nested tuple
print("Nested Tuple:", t4)
