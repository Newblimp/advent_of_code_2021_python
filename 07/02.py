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
fuel_need = {}
best_position = 0

for i in range(max_position + 1):
    if i not in fuel_need:
        fuel_need[i] = 0
    for pos in position:
        fuel_need[i] += (abs(pos - i))*(abs(pos - i)+1)//2
    if fuel_need[i] < fuel_need[best_position]:
        best_position = i

# print('The best position is: ' + str(best_position))
# print('It requiers a total of ' + str(fuel_need[best_position]) + ' fuel.')

# visualization


df = pd.DataFrame(list(fuel_need.items()), columns=['Position', 'Fuel Needed'])

sns.set_theme()

ax = sns.relplot(x='Position', y='Fuel Needed', data=df,
                 kind='line')  # , palette="Blues_d")

ax.set_axis_labels("Position", "Fuel to move all crabs into position")
ax.figure.set_size_inches(6, 4)
plt.show()
