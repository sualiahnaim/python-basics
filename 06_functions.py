#  functions in python
def greet():
    print("Hello! Welcome to Python learning.")

greet()   # fuction call

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Sualiah")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)

# Default parameter
def multiply(a, b=2):
    return a * b

print("Multiply (5, default 2):", multiply(5))
print("Multiply (5, 4):", multiply(5, 4))

# Function with multiple return values
def get_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

numbers = [10, 20, 30, 40]
total, average = get_stats(numbers)
print("Total:", total)
print("Average:", average)



