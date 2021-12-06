import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


age = [0]*9
age_old = [0]*9
with open("06/input.txt", "r") as file:
    list = file.read().split(',')
    for number in list:
        age[int(number)] += 1

backup = [age.copy()]


days = 256
for day in range(days):
    age_old = age.copy()
    for i in range(len(age)-1):
        age[i] = age_old[i+1]
    age[8] = age_old[0]
    age[6] += age_old[0]
    backup.append(age.copy())


backup_array = np.asarray(backup)
print(np.shape(backup_array))

sum = 0
for i in age:
    sum += i


number_of_fish_at_age = [str(i) for i in range(9)]

list_of_days = [str(i) for i in range(days+1)]

df = pd.DataFrame(number_of_fish_at_age, columns=['number_of_fish_at_age'])
df[list_of_days] = np.transpose(backup_array)

print(df)

sns.set_theme()
sns.set_style("dark")

# #distribution = sns.load_dataset(data)

#ax = sns.barplot(x='number_of_fish_at_age', y='256',data=df, palette="Blues_d")
# sns.despine()

# ax.set(xlabel="Age", ylabel="# of fish at age")
# ax.set_ylim([0,3*pow(10,11)])



for i in range(257):
    sns.set(rc={"figure.figsize":(8, 5)})

    ax = sns.barplot(x='number_of_fish_at_age', y=str(
        int(i)), data=df, palette="Blues_d")
    ax.set(xlabel='age in days, day ' + str(i), ylabel="# of fish, linear")#, yscale="log")
    ax.set_ylim([0, 3*pow(10, 11)])
    fig = ax.get_figure()
    fig.savefig('animation/06_lin/test' + str(i) +'.png')
    ax.clear()

for i in range(257):
    sns.set(rc={"figure.figsize":(8, 5)})

    ax = sns.barplot(x='number_of_fish_at_age', y=str(
        int(i)), data=df, palette="Blues_d")
    ax.set(xlabel='age in days, day ' + str(i), ylabel="# of fish, logarithmic", yscale="log")
    ax.set_ylim([1, 3*pow(10, 11)])
    fig = ax.get_figure()
    fig.savefig('animation/06_log/test' + str(i) +'.png')
    ax.clear()


#plt.show()


