# args - Passing multiple arguments
def sum_all(*args):
    return sum(args)

print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))


# kwargs - Passing keyword arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Sualiah", age=20, course="B.Tech CSE")


# Lambda function - Short anonymous functions
square = lambda x: x ** 2
print("Square of 5:", square(5))


# Recursion - Function calling itself
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# Docstrings - Documentation for functions
def greet(name):
    """This function greets the person passed as a parameter."""
    print(f"Hello, {name}!")

greet("Sualiah")
print("Docstring for greet function:", greet.__doc__)

