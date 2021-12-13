import numpy as np
fold = 7
coords = []
with open('13/input.txt','r') as file:
    lines = file.readlines()

for line in lines:
    str1 = line.strip().split(',')
    coords.append((int(str1[0]),int(str1[1])))

folded = []
for tupl in coords:
    if tupl[0] < 655 and tupl not in folded:
        folded.append(tupl)
    elif tupl[0] > 655 and (1310 - tupl[0], tupl[1]) not in folded:
        folded.append((1310 - tupl[0], tupl[1]))
    else:
        print('Oh no')
print(len(folded))
print(len(coords))