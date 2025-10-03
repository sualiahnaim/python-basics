# Seaborn Barplot :A Seaborn Barplot is a statistical graph that shows the average value of a numerical variable for each category of a
#  categorical variable.

import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
pokemon=pd.read_csv("pokemon_data.csv")
print(pokemon.head())
 
# Shows average speed of Legendary vs Non-Legendary Pokémon
sns.barplot(x="Legendary", y="Speed", data=pokemon)
plt.show()

# split into Legendary and Non-Legendary categories
sns.barplot(x="Legendary", y="Speed",hue="Generation" ,data=pokemon)
plt.show()

# palette='Blues_d gives a dark-to-light blue gradient
sns.barplot(x="Legendary", y="Speed",hue="Generation",palette="Blues_d" ,data=pokemon)
plt.show()
