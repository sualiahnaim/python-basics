# BOX Plot : box plot is a chart that summarizes data distribution through minimum,quartile and maximum values.


import numpy as np
from matplotlib import pyplot as plt
one=[1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[6,7,8,9,1,2,3,4]
data=list([one,two,three])
plt.boxplot(data)
plt.title("Box plot")
plt.ylabel("Values")
plt.show()

# Multiple Box Plots
group1=np.random.normal(50,10,200)
group2=np.random.normal(55,15,200)
group3=np.random.normal(60,20,200)
plt.boxplot([group1,group2,group3], labels=["Group 1", "Group 2", "Group 3"])
plt.title("Multiple Box Plots")
plt.ylabel("Values")
plt.show()

