# Violin Plot : It shows data distribution, probability density, and quartiles in a single plot.

import numpy as np
from matplotlib import pyplot as plt
one=[1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[6,7,8,9,1,2,3,4]
data=list([one,two,three])
plt.violinplot(data)
plt.title("Violin Plot")
plt.ylabel("Values")
plt.show()

# Multiple Violin Plots
group1=np.random.normal(40,5,200)
group2=np.random.normal(55,7,200)
group3=np.random.normal(65,10,200)
plt.violinplot([group1,group2,group3], showmeans=True)
plt.title("Multiple Violin Plots")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.show()
