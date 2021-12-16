import math


def expand_field(lst_input, x):
    new_lst = [[] for _ in range(x*5)]
    for j in range(5):
        for i in range(5):
            lin_c = 0
            for line in lst_input:
                for c in line.strip():
                    if int(c)+i+j < 10:
                        new_lst[j*x + lin_c].append(int(c)+i+j)
                    else:
                        new_lst[j*x + lin_c].append(int(c)+i+j-9)
                lin_c += 1
    return new_lst



#import field
with open("15/input.txt", "r") as file:
    small_field = file.readlines()


# initialize some variables to implement Dijkstra
size_x = len(small_field[0].strip())
size_y = len(small_field)
unvisited = []
nodes = {}
start = (0, 0)

# expand field according to AoC
field = expand_field(small_field, size_y)
size_x = size_x*5
size_y = size_y*5

for i in range(size_x):
    for j in range(size_y):
        unvisited.append((i, j))
        # create dictionary with distance
        nodes[(i, j)] = math.inf
nodes[start] = 0
to_visit = [start]

# calculate distance to all other nodes, append to dictionary
while len(to_visit) > 0:

    i,j = to_visit[0] # about twice as fast as actually looking for the minimum

    # looks through dict and takes node with min weight
    # i, j = min(to_visit, key = lambda k: nodes[k])

    if i > 0:
        if nodes[(i, j)] + int(field[i-1][j]) < nodes[(i-1, j)]:
            nodes[(i-1, j)] = nodes[(i, j)] + int(field[i-1][j])
            to_visit.append((i-1, j))

    if j > 0:
        if nodes[(i, j)] + int(field[i][j-1]) < nodes[(i, j-1)]:
            nodes[(i, j-1)] = nodes[(i, j)] + int(field[i][j-1])
            to_visit.append((i, j-1))

    if i < (size_x - 1):
        if nodes[(i, j)] + int(field[i+1][j]) < nodes[(i+1, j)]:
            nodes[(i+1, j)] = nodes[(i, j)] + int(field[i+1][j])
            to_visit.append((i+1, j))

    if j < (size_y - 1):
        if nodes[(i, j)] + int(field[i][j+1]) < nodes[(i, j+1)]:
            nodes[(i, j+1)] = nodes[(i, j)] + int(field[i][j+1])
            to_visit.append((i, j+1))

    to_visit.remove((i,j))

print(nodes[(size_x-1,size_y-1)])