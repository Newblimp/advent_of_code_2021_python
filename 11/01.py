from os import linesep
import numpy as np

def flash(octopus_field, grid_size):
    for i in range(grid_size):
        for j in range(grid_size):
            if octopus_field[i][j] == 9:
                octopus_field[i][j] = 10
                if i > 1 and j > 1:
                    if octopus_field[i-1][j-1] < 9: octopus_field[i-1][j-1] += 1  
                if j > 1:
                    if octopus_field[i][j-1] < 9: octopus_field[i][j-1] += 1 
                if i < (grid_size-1) and j > 1:
                    if octopus_field[i+1][j-1] < 9: octopus_field[i+1][j-1] += 1 
                if i > 1:
                    if octopus_field[i-1][j] < 9: octopus_field[i-1][j] += 1 
                if i < (grid_size-1):
                    if octopus_field[i+1][j] < 9: octopus_field[i+1][j] += 1 
                if i > 1 and j < (grid_size-1):
                    if octopus_field[i-1][j+1] < 9: octopus_field[i-1][j+1] += 1 
                if j < (grid_size-1):
                    if octopus_field[i][j+1] < 9: octopus_field[i][j+1] += 1 
                if i < (grid_size-1) and j < (grid_size-1):
                    if octopus_field[i+1][j+1] < 9: octopus_field[i+1][j+1] += 1 
        

grid_size = 10

octopi = np.zeros((10, 10))

with open("11/test.txt", "r") as file:
    lines = file.readlines()
    for i in range(grid_size):
        for j in range(grid_size):
            octopi[i][j] = int(lines[i][j])

# implement description of one step here
# First, the energy level of each octopus increases by 1.
octopi = octopi + 1

# Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
print(octopi)

flash(octopi, grid_size)
print(octopi)
