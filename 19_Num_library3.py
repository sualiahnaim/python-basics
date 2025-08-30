# NumPy Mathematics Operations
# Addition of Numpy Arrays
import numpy as np
n1=np.array([10,20])
n2=np.array([30,40])
n3=np.sum([n1,n2])   # Sum of all elements from n1 and n2
print(n3)

# Add only Column values
n4=np.sum([n1,n2],axis=0)
print(n4)

# Add only rows values
n5=np.sum([n1,n2],axis=1)
print(n5)

# Arithmatic operations 
n6=np.array([10,20,30])   
n7=n6+5               # Addition
print(n7)
n8=n6-5               # Subtraction
print(n8)
n9=n6*2               # Multiplication
print(n9)
n10=n6/2              # Division
print(n10)

# Math functions
n11=np.random.randint(1,50,10)
n12=np.mean(n11)
print(n12)         # Mean
n13=np.median(n11)
print(n13)         # Median
n14=np.std(n11)    # Standard Deviation
print(n14)


