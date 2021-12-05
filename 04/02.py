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
squares_backup = squares

#determine winner board
used_up = [0]*len(squares)
for drawn in drawn_list:
	for i in range(len(squares)):
		for j in range(n):
			sum_x = 0
			sum_y = 0 
			for k in range(n):
				if squares[i][j][k] == int(drawn):
					tracker[i][j][k] = 1
				sum_x += tracker[i][j][k]
				sum_y += tracker[i][k][j]
				if ((sum_x == 5) or (sum_y == 5)) and (used_up[i] == 0):
					winner = i
					last_number = drawn
					solution = squares[i]
					used_up[i] = 1
					#squares_backup = np.delete(squares_backup, winner, 0)
#					tracker = np.delete(tracker, winner, 0)
					#print(winner)
	# 				break
	# 		else:
	# 			continue
	# 		break
	# 	else:
	# 		continue
	# 	break
	# if len(squares) == 0:
	# 	break


final_tracker = np.zeros_like(solution)
for drawn in drawn_list:
	for i in range(n):
		sum_x = 0
		sum_y = 0 
		for j in range(n):
			if solution[i][j] == int(drawn):
				final_tracker[i][j] = 1
			sum_x += final_tracker[i][j]
			sum_y += final_tracker[j][i]
			if (sum_x == 5) or (sum_y == 5):
				print('it should break here')
				break
				print("But it doesn't")
		if (sum_x == 5) or (sum_y == 5):
			print('it should break here')
			break
			print("But it doesn't")
	if (sum_x == 5) or (sum_y == 5):
		print('it should break here')
		break
		print("But it doesn't")

sum = 0
for j in range(n):
	for k in range(n):
		if final_tracker[j][k] == 0:
			sum += solution[j][k]
print(sum)
print(drawn)
print(int(drawn)*sum)


# sum = 0
# print(winner)
# #print(squares[winner])
# for j in range(n):
# 	for k in range(n):
# 		if solution_bool[winner][j][k] == 0:
# 			sum += solution[winner][j][k]
# print(solution)
# print(last_number)
# print(sum)





#for drawn in drawn_list:
#	result = np.where(squares == int(drawn))
	#print(drawn)
	#print(result)
#	for index in range(0,len(result)):
#		print(result[index])