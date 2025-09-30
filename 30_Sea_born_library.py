# Seaborn : Seaborn is a powerful Python data visualization library built on top of Matplotlib. 

import seaborn as sns
from matplotlib import pyplot as plt
fmri=sns.load_dataset("fmri")
print(fmri.head())     # for upper five records
sns.lineplot(x="timepoint", y="signal", data=fmri)  # Automatically labelled
plt.show()

# Grouping data with 'hue'
sns.lineplot(x="timepoint", y="signal", data=fmri, hue='event')
plt.show()

# Adding Style
sns.lineplot(x="timepoint",y="signal", data=fmri, hue='event', style='event')
plt.show()

# Adding Markers
sns.lineplot(x="timepoint",y="signal", data=fmri, hue='event', style='event', markers=True)
plt.show()
