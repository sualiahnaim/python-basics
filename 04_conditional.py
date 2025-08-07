# Conditional Statements in Python

# if without else
age = int(input("Enter your age :"))
if age >= 18:                         
    print("You are eligible to vote.")

# if-else
marks = int(input("Enter your Marks :"))
if marks >= 50:
    print("You passed.")
else:
    print("You failed.")

# if-elif-else
num = int(input("Enter the Number :"))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Nested if
x = int(input("Enter the value of x :"))
if x > 0:
    if x < 20:
        print("x is between 0 and 20")
    else:
        print("Please entered only 0 to 20 number")

# Logical operators
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
if a > 0 and b > 0:
    print("Both a and b are positive")

if not a == b:
    print("a is not equal to b")
