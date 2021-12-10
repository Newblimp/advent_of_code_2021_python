import numpy as np

def find_basins(field1):
    tracker = np.zeros_like(field1)
    basins = [[(0,0)]]
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != 9:
                for outer in basins:
                    if (i,j) not in outer:
                        member_of_basin = true
                        if (i-1,j) in outer:
                            outer.append((i,j))
                        elif (i+1,j) in outer:
                            outer.append((i,j))
                        elif (i,j-1) in outer:
                            outer.append((i,j))
                        elif (i,j+1) in outer:
                            outer.append((i,j))
                        else:
                            member_of_basin = false
    return basins

            

def lowpoints_risk(field1):
    risk = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            lowest = True
            if i > 0:
                if field[i-1][j] <= field[i][j]:
                    lowest = False
            if j > 0:
                if field[i][j-1] <= field[i][j]:
                    lowest = False
            if i < len(field) - 1:
                if field[i+1][j] <= field[i][j]:
                    lowest = False
            if j < len(field[0]) - 1:
                if field[i][j+1] <= field[i][j]:
                    lowest = False

            if lowest:
                risk += field[i][j] + 1
    return risk


with open("09/test.txt", "r") as file:
    rows = file.readlines()
    field = np.zeros(shape=(len(rows), len(rows[0].strip())))
    x = 0
    y = 0
    for line in rows:
        for c in line.strip():
            field[y][x] = int(c)
            x += 1
        y += 1
        x = 0

cumulative_risk = find_basins(field)

print(cumulative_risk)
