# Matplotlib Library : Matplotlib is a python library used for data visualization.

# Line Plot : A line plot is a fundamental type of graph used to visualize data points connected by straight line segments
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,11)
y=3*x
plt.plot(x,y)
plt.show()

# How to labelled
plt.plot(x,y , color='red', linestyle=':', linewidth=5)
plt.title("X VS Y")
plt.xlabel("This is X-axis")
plt.ylabel("This is Y-axis")
plt.show()

# Add two plots
y1=2*x
y2=3*x
plt.plot(x,y1, color='green', linestyle=':')
plt.plot(x,y2, color="yellow", linewidth=4)
plt.grid(True)
plt.title("Two lines in a plot")
plt.ylabel("This is y-axis")
plt.show()

# Adding sub plots
plt.subplot(2,1,1)
plt.plot(x,y1, color='red', linestyle=':')
plt.plot(x,y2, color='blue', linewidth=3)
plt.title("Two lines in a plot")
plt.xlabel("This is x-axis")
plt.ylabel("This is y-axis")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(x,y1, color='orange', linestyle=':')
plt.plot(x,y2, color='white', linewidth=4)
plt.title("Two lines in a plot")
plt.xlabel("This is x-axis")
plt.ylabel("This is y-axis")
plt.grid(True)
plt.show()
