def fold(coordinate_tuples,x,fold_dir):
    folded_list = []
    for tupl in coordinate_tuples:
        if fold_dir == 'x':
            if tupl[0] < x and tupl not in folded_list:
                folded_list.append(tupl)
            elif tupl[0] > x and (2*x - tupl[0], tupl[1]) not in folded_list:
                folded_list.append((2*x - tupl[0], tupl[1]))
        if fold_dir == 'y':
            if tupl[1] < x and tupl not in folded_list:
                folded_list.append(tupl)
            elif tupl[1] > x and (tupl[0], 2*x - tupl[1]) not in folded_list:
                folded_list.append((tupl[0], 2*x - tupl[1]))
    return folded_list


coords = []
with open('13/input.txt','r') as file:
    lines = file.readlines()

for line in lines:
    str1 = line.strip().split(',')
    coords.append((int(str1[0]),int(str1[1])))

folded = [(655,'x'),(447,'y'),(327,'x'),(223,'y'),(163,'x'),(111,'y'),(81,'x'),(55,'y'),(40,'x'),(27,'y'),(13,'y'),(6,'y')]
# folded = [(7,'y'), (5,'x')]

for tpl in folded:
    coords = fold(coords,tpl[0],tpl[1])

import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

field = np.ones((40,6))

for tpl in coords:
    field[tpl[0],tpl[1]] = 0

for i in range(35,40):
    print(field[i])


