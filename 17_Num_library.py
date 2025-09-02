# Numpy Library : Numpy stands for Numerical python and is the core library for numeric and scientific computing

# Create array using numpy
import numpy as np
l1=[1,2,3,4,5,6]
n1=np.array(l1)    # 1D Array
print(n1)
n2=np.array([[1,2,3,4,5],[5,4,3,2,1]])     # 2D Array
print(n2)

# Initializing Numpy array with zero
n3=np.zeros((2,3))      # Each element in this array is zero
print(n3)
 
# Initializing Numpy array with same number 
n4=np.full((3,3),70)    # Each element in this array is 70
print(n4)

# Initializing Numpy array within a range
n5=np.arange(10,20)
print(n5)
n6=np.arange(50,500,10)  ## 50 se 490 tak numbers 10-10 ke gap me generate karega (1D array)
print(n6)

# Initializing Numpy array with random numbers
n7=np.random.randint(100,200,10)  ## 100 se 199 ke beech ke 10 random integers generate karega (1D array)
print(n7)

# Find Shape of array
n8=np.random.randint(20,50,10)
print(n8)
print(n8.shape)


