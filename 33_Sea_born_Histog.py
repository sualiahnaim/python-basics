# Seaborn Histogram : A histogram in Seaborn is a type of plot that shows the distribution of a numerical variable by dividing the data into intervals.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pokemon=pd.read_csv("pokemon_data.csv")
print(pokemon.head())

sns.displot(pokemon["Attack"])
plt.show()

# Only frequency without histogram
sns.displot(pokemon["Attack"], kind="kde")
plt.show()
