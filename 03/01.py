pos = 0
bits = [0]*12
for line in open("input.txt","r"):
	for i in line.strip():
		if int(i) == 1:
			bits[pos] += 1
		else:
			bits[pos] -= 1
		pos += 1
	pos = 0
print(bits)
#calculate gamma rate
gamma = 0
pos2 = 11
for i in bits:
	if i > 0:
		gamma += pow(2,(pos2))
	pos2 -= 1

#calculate epsilon rate
epsilon = 0
pos3 = 11
for i in bits:
	if i < 0:
		epsilon += pow(2,(pos3))
	pos3 -= 1

print('The power consumption of the submarine is: ' + str(epsilon*gamma))