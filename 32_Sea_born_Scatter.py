# Seaborn Scatterplot : A scatter plot in Seaborn is a powerful way to visualize the relationship between two continuous variables.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

iris=pd.read_csv("iris.csv")
print(iris.head())

# scatterplot showing relationship between sepal_length and petal_length
sns.scatterplot(x="sepal_length", y="petal_length", data=iris)
plt.show()

# Scatterplot with color differentiation (hue) based on species
sns.scatterplot(x="sepal_length", y="petal_length", data=iris, hue="species")
plt.show()

# Scatterplot with color differentiation (hue) based on Petal length
sns.scatterplot(x="sepal_length", y="petal_length", data=iris, hue="petal_length")
plt.show()

