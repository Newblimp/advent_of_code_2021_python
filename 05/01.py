import numpy as np

n = 1000
field = np.zeros((n,n))
for line in open("input.txt","r"):
	components = line.split()
	pos_1 = components[0].split(',')
	pos_2 = components[2].split(',')
	if (pos_1[0] == pos_2[0]) and (int(pos_1[1]) <= int(pos_2[1])):
		for i in range(int(pos_1[1]),int(pos_2[1])+1):
			field[int(pos_1[0])][i] += 1
	if (pos_1[0] == pos_2[0]) and (int(pos_1[1]) > int(pos_2[1])):
		for i in range(int(pos_2[1]),int(pos_1[1])+1):
			field[int(pos_1[0])][i] += 1
	if (pos_1[1] == pos_2[1]) and (int(pos_1[0]) <= int(pos_2[0])):
		for i in range(int(pos_1[0]),int(pos_2[0])+1):
			field[i][int(pos_1[1])] += 1
	if (pos_1[1] == pos_2[1]) and (int(pos_1[0]) > int(pos_2[0])):
		for i in range(int(pos_2[0]),int(pos_1[0])+1):
			field[i][int(pos_1[1])] += 1

result = 0
for i in range(n):
	for j in range(n):
		if field[i][j] > 1:
			result += 1
print(result)