counter = 0
with open("input.txt","r") as file:
	lines = file.readlines()
	old_line = int(lines[0])
	lines.pop(0)
	for line in lines:
		if int(line) > old_line:
			counter += 1
		old_line = int(line)
print(counter)
