# Bar Plot : A bar plot is a graphical repesentation of data using rectangular bars.

import numpy as np
from matplotlib import pyplot as plt
students={'Sualiah':84, 'Yuvraj':45, 'Ram':65, 'Matt':49}
name=list(students.keys())
values=list(students.values())
plt.bar(name,values)
plt.show()

# How to labelled
plt.title("Distribution of Marks")
plt.xlabel("Names of Students")
plt.ylabel("Marks of Students")
plt.bar(name,values, color='green')
plt.show()

# Barplot ko agr horizontal bnana ho tb
plt.title("Distribution of Marks")
plt.xlabel("Names of Students")
plt.ylabel("Marks of Students")
plt.barh(name,values, color='yellow')
plt.show()
