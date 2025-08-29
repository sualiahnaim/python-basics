# Python Library : Python library is a collection of functions and methods that allows you to perform many actions without writing your code

# Joining Numpy Array
import numpy as np
n1=np.random.randint(20,70,10)
n2=np.random.randint(10,60,10)
n3=np.vstack((n1,n2))  # Joining the arrays vertically (row-wise)
print(n3)

n4=np.hstack((n1,n2)) # Joining the arrays horizontally (column-wise / side by side)
print(n4)

n5=np.column_stack((n1,n2)) # Joining the arrays as columns (2D array, side by side in column form)
print(n5)
 
# Intersection of array 
n6=np.arange(10,70,10)
n7=np.arange(50,100,10)
n8=np.intersect1d(n6,n7)
print(n8)

# Difference of array
n9=np.setdiff1d(n6,n7)
print(n9)
n10=np.setdiff1d(n7,n6)
print(n10)


