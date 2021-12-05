window_measurements = 0
old_window_measurements = 0
counter = 0

with open("input.txt","r") as file:
	measurements = file.readlines()
	old_window_measurements = int(measurements[0]) + int(measurements[1]) + int(measurements[2])
	for i in range(1,len(measurements) - 2):
		window_measurements = int(measurements[i]) + int(measurements[i+1]) + int(measurements[i+2])
		if window_measurements > old_window_measurements:
			counter += 1
		old_window_measurements = window_measurements
		window_measurements = 0
print(counter)