# Dictionaries in Python

student = {
    "name": "Sualiah",
    "age": 20,                                   #  Creating a dictionary
    "course": "B.Tech CSE",
    "university": "TMU Moradabad"
}
print("Dictionary:", student)

print("Name:", student["name"])                   # Accessing values
print("Age:", student.get("age"))

student["age"] = 21                               # Update           
student["hobby"] = "Coding"                       # Add new key
print("Updated Dictionary:", student)

student.pop("course")                        # Removing items
print("After pop:", student)

print("\nKeys:")                            # Looping through dictionary
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey & Values:")
for key, value in student.items():
    print(key, ":", value)

# Dictionary methods
keys = list(student.keys())
values = list(student.values())
print("Keys list:", keys)
print("Values list:", values)

students = {
    "student1": {"name": "Aman", "age": 18},              # Nested dictionary
    "student2": {"name": "Sualiah", "age": 20}
}
print("Nested Dictionary:", students)


