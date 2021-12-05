import numpy as np

#size of bingo board
n = 5;

#read file and load bingo boards into numpy array
with open("input.txt","r") as file:
	drawn_list = file.readline().split(',')
	numbers = file.read().split()
	squares = np.empty([(len(numbers)//(n*n)),n,n], dtype=int)
	
	#get the numbers into an array
	for i in range(len(numbers)//(n*n)):
		for j in range(n):
			for k in range(n):
				squares[i][j][k] = int(numbers[(j*n + k) + i*(n*n)])

sum_x = 0
sum_y = 0
tracker = np.zeros_like(squares)

#determine winner board
for drawn in drawn_list:
	for i in range(len(numbers)//(n*n)):
		for j in range(n):
			sum_x = 0
			sum_y = 0 
			for k in range(n):
				if squares[i][j][k] == int(drawn):
					tracker[i][j][k] = 1
				sum_x += tracker[i][j][k]
				sum_y += tracker[i][k][j]
				if (sum_x == 5) or (sum_y == 5):
					winner = i
					last_number = drawn
					print(winner)
					break
			else:
				continue
			break
		else:
			continue
		break
	else:
		continue
	break

sum = 0
for j in range(n):
	for k in range(n):
		if tracker[winner][j][k] == 0:
			sum += squares[winner][j][k]
print(sum)
print(drawn)
print(sum*int(drawn))


#for drawn in drawn_list:
#	result = np.where(squares == int(drawn))
	#print(drawn)
	#print(result)
#	for index in range(0,len(result)):
#		print(result[index])