import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

position = []
max_position = 0
with open("07/input.txt", "r") as file:
    text = file.read().split(',')
    for c in text:
        position.append(int(c))
        if int(c) > max_position:
            max_position = int(c)

# print(max_position)
# cycle through each position, sum up fuel needs and determine smallest fuel need

# key = position, value = fuel needed
fuel_need1 = {}
fuel_need2 = {}

for i in range(max_position + 1):
    if i not in fuel_need2:
        fuel_need2[i] = 0
    if i not in fuel_need1:
        fuel_need1[i] = 0
    for pos in position:
        fuel_need2[i] += (abs(pos - i))*(abs(pos - i)+1)//2
        fuel_need1[i] += abs(pos - i)


# visualization


df = pd.DataFrame(list(fuel_need1.items()), columns=['Position', '#1'])
df2 = pd.DataFrame(list(fuel_need2.items()), columns=[
                   'Position', 'Fuel Needed'])

df['#2'] = df2['Fuel Needed']

dfm = df.melt('Position', var_name='cols', value_name='vals')

print(dfm)
sns.set_theme(style="ticks")

ax = sns.relplot(data=dfm, x='Position', y='vals', hue='cols',
                 kind='line')  # , palette="Blues_d")

ax.set_axis_labels("Position", "Fuel to move all crabs into position")
ax.legend.set_title("Puzzle")

# ax.figure.set_size_inches(6, 4)
ax.ax.margins(.15)
ax.despine(trim=False)
ax.set(yscale='log', ylim=(pow(10, 5), pow(10, 9)))
plt.show()
