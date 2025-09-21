# Pie Chart : Pie chart is a circular chart divided into slices to represent proportional data or percentages.
# Doughnut Chart : Doughnut Chart is a pie chart with a hole in the center.

import numpy as np
from matplotlib import pyplot as plt
fruit=['Apple','Mango','Guava','Orange']
Quantity=[10,5,15,20]
plt.pie(Quantity, labels=fruit)
plt.title("Pie Chart")
plt.show()

# Pie Chart with percentages
sizes=[40,30,20,10]
labels=["Python", "Java", "C++", "Others"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart with percentages")
plt.show()

# Donut Chart (Advanced pie chart)
sizes=[40,30,20,10]
labels=["Chrome","Edge","Firefox","Others"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, wedgeprops=dict(width=0.4))
plt.title("Donut Chart")
plt.show()
