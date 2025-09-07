# Scatter plot : Scatter plot is a graph that uses dots to visualize the relationship between two numerical variables.

import numpy as np
from matplotlib import pyplot as plt
x=[4,2,5,7,2,4,6,2,7,9]
y=[9,3,5,1,8,5,4,3,7,1]
plt.scatter(x,y)
plt.show()

# Changing Mark Aesthetics
plt.scatter(x,y,marker='*',color='red',s=100)
plt.show()

# Add two scatter in same graph
a=np.random.randint(1,20,10)
b=np.random.randint(2,21,10)
c=np.random.randint(3,22,10)
plt.scatter(a,b, marker='*', color='yellow', s=100)
plt.scatter(a,c, color='pink', s=200)
plt.show()

# Adding Sub plots
plt.subplot(1,2,1)
plt.scatter(a,b, marker='*', s=200)
plt.subplot(1,2,2)
plt.scatter(a,c, s=200)
plt.show()
