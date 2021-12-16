import math

#import field
with open("15/input.txt","r") as file:
    field = file.readlines()



#initialize some variables to implement Dijkstra
size_x = len(field[0].strip())
size_y = len(field)
visited = []
# unvisited = []
nodes = {}
start = (0,0)
for i in range(size_x):
    for j in range(size_y):
        # unvisited.append((i,j))
        nodes[(i,j)] = [math.inf] #create dictionary with distance and later append connecting node
nodes[start] = [0]



#calculate distance to all other nodes, append to dictionary
for i in range(size_x):
    for j in range(size_y):
        if i > 0 and (i-1,j) not in visited:
            if nodes[(i,j)][0] + int(field[i-1][j]) < nodes[(i-1,j)][0]:
                nodes[(i-1,j)][0] = nodes[(i,j)][0] + int(field[i-1][j])
                if len(nodes[(i-1,j)]) == 1:
                    nodes[(i-1,j)].append((i,j))
                else:
                    nodes[(i-1,j)][1] = (i,j)

        if j > 0 and (i,j-1) not in visited:
            if nodes[(i,j)][0] + int(field[i][j-1]) < nodes[(i,j-1)][0]:
                nodes[(i,j-1)][0] = nodes[(i,j)][0] + int(field[i][j-1])
                if len(nodes[(i,j-1)]) == 1:
                    nodes[(i,j-1)].append((i,j))
                else:
                    nodes[(i,j-1)][1] = (i,j)

        if i < (size_x - 1) and (i+1,j) not in visited:
            if nodes[(i,j)][0] + int(field[i+1][j]) < nodes[(i+1,j)][0]:
                nodes[(i+1,j)][0] = nodes[(i,j)][0] + int(field[i+1][j])
                if len(nodes[(i+1,j)]) == 1:
                    nodes[(i+1,j)].append((i,j))
                else:
                    nodes[(i+1,j)][1] = (i,j)

        if j < (size_y - 1) and (i,j+1) not in visited:
            if nodes[(i,j)][0] + int(field[i][j+1]) < nodes[(i,j+1)][0]:
                nodes[(i,j+1)][0] = nodes[(i,j)][0] + int(field[i][j+1])
                if len(nodes[(i,j+1)]) == 1:
                    nodes[(i,j+1)].append((i,j))
                else:
                    nodes[(i,j+1)][1] = (i,j)
        
        visited.append((i,j))

print(nodes[(size_x-1, size_y-1)])