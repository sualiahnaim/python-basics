#Loops in Python

# 1. For Loop Basics
print("For Loop Example:")
for i in range(5):
    print(i)

# 2. Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("\nIterating over a list:")
for fruit in fruits:
    print(fruit)

# 3. While Loop Basics
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print(count)
    count += 1

# 4. Break Statement
print("\nBreak Statement Example:")
for num in range(10):
    if num == 5:
        break
    print(num)

# 5. Continue Statement
print("\nContinue Statement Example:")
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# 6. Nested Loops (Multiplication Table)
print("\nMultiplication Table (1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()

