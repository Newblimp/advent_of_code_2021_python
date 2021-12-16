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
start = (0, 0)

# expand field according to AoC
field = expand_field(small_field, size_y)
size_x = size_x*5
size_y = size_y*5


nodes = {(i, j): math.inf for i in range(size_x) for j in range(size_y)}
nodes[start] = 0
# to_visit = [start]
buckets = {0: [start]}

# calculate distance to all other nodes, append to dictionary
while len(buckets) > 0:

    # looks through dict and takes node with min weight
    key_min_value = min(buckets)
    i, j = buckets[key_min_value][0]

    if i > 0:
        if nodes[(i, j)] + int(field[i-1][j]) < nodes[(i-1, j)]:
            nodes[(i-1, j)] = nodes[(i, j)] + int(field[i-1][j])
            if nodes[(i-1,j)] not in buckets:
                buckets[nodes[(i-1, j)]] = [(i-1, j)]
            else:
                buckets[nodes[(i-1,j)]].append((i-1, j))

    if j > 0:
        if nodes[(i, j)] + int(field[i][j-1]) < nodes[(i, j-1)]:
            nodes[(i, j-1)] = nodes[(i, j)] + int(field[i][j-1])
            if nodes[(i,j-1)] not in buckets:
                buckets[nodes[(i, j-1)]] = [(i, j-1)]
            else:
                buckets[nodes[(i,j-1)]].append((i, j-1))

    if i < (size_x - 1):
        if nodes[(i, j)] + int(field[i+1][j]) < nodes[(i+1, j)]:
            nodes[(i+1, j)] = nodes[(i, j)] + int(field[i+1][j])
            if nodes[(i+1,j)] not in buckets:
                buckets[nodes[(i+1, j)]] = [(i+1, j)]
            else:
                buckets[nodes[(i+1,j)]].append((i+1, j))

    if j < (size_y - 1):
        if nodes[(i, j)] + int(field[i][j+1]) < nodes[(i, j+1)]:
            nodes[(i, j+1)] = nodes[(i, j)] + int(field[i][j+1])
            if nodes[(i,j+1)] not in buckets:
                buckets[nodes[(i, j+1)]] = [(i, j+1)]
            else:
                buckets[nodes[(i,j+1)]].append((i, j+1))

    buckets[key_min_value].remove((i,j))
    if len(buckets[key_min_value]) == 0:
        buckets.pop(key_min_value)

print(nodes[(size_x-1, size_y-1)])
