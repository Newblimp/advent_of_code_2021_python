def visit_small_cave(pathlist, current_cave):
    freq = small_cave_freq(pathlist)
    reached_max = reached_two(freq)
    if current_cave not in freq:
        freq[current_cave] = 0
    if not reached_max:
        if freq[current_cave] <= 1:
            return True
        return False
    else:
        if freq[current_cave] < 1:
            return True
        return False

def small_cave_freq(pathlist):
    d = {}
    for cave in pathlist:
        if cave == cave.lower():
            if cave not in d:
                d[cave] = 1
            else:
                d[cave] += 1
    return d

def num_freq_larger_one(diction):
    counter = 0
    for cave in diction:
        if diction[cave] > 1:
            counter += 1
    return counter

def reached_two(diction):
    for cave in diction:
        if diction[cave] >= 2:
            return True
    return False

    
with open('12/input.txt','r') as file:
    lines = file.readlines()
    connects = []
    for path in lines:
        connects.append(path.strip().split('-'))

connections = {}
for pair in connects:
    if pair[0] not in connections:
        connections[pair[0]] = [pair[1]]
    else:
        connections[pair[0]].append(pair[1])
    if pair[1] not in connections:
        connections[pair[1]] = [pair[0]]
    else:
        connections[pair[1]].append(pair[0])

#   go through entire list of paths
#       pick last element from path
#       for each possible connection:
#           create new paths with old path + new place
#           append to newpath list
#   replace paths list with new paths
paths = [['start']]
reached_end = False
visited_caves = ['start']
finished_paths = []
while not reached_end:
    reached_end = True
    new_paths = []
    for path in paths:
        # print(path)
        for new_cave in connections[path[-1]]:
            if new_cave == 'end':
                finished_paths.append(path + [new_cave])
            elif new_cave != 'start' and (visit_small_cave(path,new_cave) or new_cave != new_cave.lower()):
                new_paths.append(path + [new_cave])
    if len(new_paths) != 0:
        reached_end = False
        paths = new_paths

print(len(finished_paths))