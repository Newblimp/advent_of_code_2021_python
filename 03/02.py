pos_line = 0
bitcount = 0
#determinee oxygen generator rating
with open("input.txt","r") as file:
	lines = file.readlines()
	for pos in range(len(lines[0].strip())):
		#loop to get most frequent bit
		for line in lines:
			if line[pos] == '1':
				bitcount += 1
			else:
				bitcount -= 1
		#loop to kick lines out
		pos_line = 0
		pos_list = []
		for line in lines:
			if bitcount > 0 or bitcount == 0:
				if line[pos] == '1':
					pos_line += 1
				else:
					pos_list.append(pos_line)
			if bitcount < 0:
				if line[pos] == '0':
					pos_line += 1
				else:
					pos_list.append(pos_line)
		for _ in pos_list:
			lines.pop(_)
		if len(lines) == 1:
			break
		pos_line = 0
		pos_list = []
		bitcount = 0

	#calculate oxygen_generator_rating
	oxygen = 0
	pos2 = len(lines[0].strip()) - 1
	for i in lines[0].strip():
		if int(i) > 0:
			oxygen += pow(2,(pos2))
		pos2 -= 1
	print(oxygen)


#determine CO2 scrubber rating
with open("input.txt","r") as file:
	lines = file.readlines()
	for pos in range(len(lines[0].strip())):
		#loop to get most frequent bit
		for line in lines:
			if line[pos] == '1':
				bitcount += 1
			else:
				bitcount -= 1
		#loop to kick lines out
		pos_line = 0
		pos_list = []
		for line in lines:
			if bitcount < 0:
				if line[pos] == '1':
					pos_line += 1
				else:
					pos_list.append(pos_line)
			if bitcount > 0 or bitcount == 0:
				if line[pos] == '0':
					pos_line += 1
				else:
					pos_list.append(pos_line)
		for _ in pos_list:
			lines.pop(_)
		if len(lines) == 1:
			break
		pos_line = 0
		pos_list = []
		bitcount = 0
	#calculate oxygen_generator_rating
	CO2 = 0
	pos3 = len(lines[0].strip()) - 1
	for i in lines[0].strip():
		if int(i) > 0:
			CO2 += pow(2,(pos3))
		pos3 -= 1
	print(CO2)
print(oxygen*CO2)





# 	bits = [0]*len(file.readline().strip())
# 	lines = file.readlines()
# 	for line in lines:
# 		for i in line.strip():
# 			if int(i) == 1:
# 				bits[pos] += 1
# 			else:
# 				bits[pos] -= 1
# 			pos += 1
# 		pos = 0
# 	for bit in bits:
# 		if int(bit) > 0:
# 			bits[pos] = 1
# 		else if int(bit) < 0:
# 			bits[pos] = 0
# 		else:
# 			print(CAREFUL!! NUMBER OF 1 & 0 IS THE SAME!)


# print(bits)

#calculate gamma rate
# gamma = 0
# pos2 = 11
# for i in bits:
# 	if i > 0:
# 		gamma += pow(2,(pos2))
# 	pos2 -= 1

# #calculate epsilon rate
# epsilon = 0
# pos3 = 11
# for i in bits:
# 	if i < 0:
# 		epsilon += pow(2,(pos3))
# 	pos3 -= 1

# print('The power consumption of the submarine is: ' + str(epsilon*gamma))