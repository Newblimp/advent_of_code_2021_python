import numpy as np

def flash(octopus_field, grid_size, counter):
    for i in range(grid_size):
        for j in range(grid_size):
            if octopus_field[i][j] > 9:
                octopus_field[i][j] = 0
                counter += 1
                if i > 0 and j > 0:
                    if octopus_field[i-1][j-1] != 0: octopus_field[i-1][j-1] += 1  
                if j > 0:
                    if octopus_field[i][j-1] != 0: octopus_field[i][j-1] += 1 
                if i < (grid_size-1) and j > 0:
                    if octopus_field[i+1][j-1] != 0: octopus_field[i+1][j-1] += 1 
                if i > 0:
                    if octopus_field[i-1][j] != 0: octopus_field[i-1][j] += 1 
                if i < (grid_size-1):
                    if octopus_field[i+1][j] != 0: octopus_field[i+1][j] += 1 
                if i > 0 and j < (grid_size-1):
                    if octopus_field[i-1][j+1] != 0: octopus_field[i-1][j+1] += 1 
                if j < (grid_size-1):
                    if octopus_field[i][j+1] != 0: octopus_field[i][j+1] += 1 
                if i < (grid_size-1) and j < (grid_size-1):
                    if octopus_field[i+1][j+1] != 0: octopus_field[i+1][j+1] += 1 
    return counter
        



grid_size = 10

octopi = np.zeros((grid_size, grid_size))

with open("11/input.txt", "r") as file:
    lines = file.readlines()
    for i in range(grid_size):
        for j in range(grid_size):
            octopi[i][j] = int(lines[i][j])

# loop 100 times
counter = 0
first_sync = 0
i = 0
while first_sync == 0:
    i += 1
    # implement description of one step here
    # First, the energy level of each octopus increases by 1.
    octopi = octopi + 1

    # Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
    # print(octopi)
    while (np.any(octopi > 9)):
        counter = flash(octopi, grid_size, counter)
    if np.all(octopi == octopi[0][0]):
        first_sync = i 
        break

    

print(first_sync)
