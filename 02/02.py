horizontal_position = 0
depth = 0
aim = 0
with open("input.txt","r") as file:
	lines = file.readlines()
	for line in lines:
		command = line.split()
		if command[0] == 'forward':
			horizontal_position += int(command[1])
			depth += aim*int(command[1])
		if command[0] == 'down':
			aim += int(command[1])
		if command[0] == 'up':
			aim -= int(command[1])
print(horizontal_position)
print(depth)
print("The resulting position multiplied by the depth is: " + str(depth*horizontal_position))