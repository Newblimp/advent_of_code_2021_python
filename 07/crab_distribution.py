import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

positions = []
with open("07/input.txt", "r") as file:
    text = file.read().split(',')
    for position in text:
        positions.append(int(position))

bin_resolution = 25
binned_positions = {}

for pos in positions:
    if (pos//bin_resolution)*bin_resolution not in binned_positions:
        binned_positions[(pos//bin_resolution)*bin_resolution] = 0
    binned_positions[(pos//bin_resolution)*bin_resolution] += 1

df = pd.DataFrame(list(binned_positions.items()),
                  columns=['Position', 'Number'])

sns.set_theme(style="ticks")

ax = sns.relplot(data=df,x='Position',y='Number',kind='line')
ax.set_axis_labels("Position","Number of crabs")

ax.ax.margins(.15)
ax.despine(trim=True)

plt.show()
