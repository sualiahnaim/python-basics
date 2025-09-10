# Histogram : Histogram is a visual representation of the distribution of quantitative data.

import numpy as np
from matplotlib import pyplot as plt
data=[2,2,2,2,2,2,5,5,5,8,4,8,4,5,9,9,9,1,5,]
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Histogram with multiple dataset
data1=np.random.randn(1000)
data2=np.random.randn(1000)+2
plt.hist([data1,data2], color=['skyblue','orange'])
plt.table("Multiple histogram")
plt.xlabel("Values")
plt.ylabel("Frequencyy")
plt.legend()
plt.show()

# Normalized histogram (Density)
data3=np.random.randn(1000)
plt.hist(data3, bins=20, density=True, color='green', alpha=0.6,edgecolor="black")
plt.title("Normalized histogram (Probability Density)")
plt.xlabel("Values")
plt.ylabel("Density")
plt.show()

