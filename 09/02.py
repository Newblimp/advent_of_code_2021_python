import numpy as np

def find_basins(field1):
    tracker = np.zeros_like(field1)
    basins = [[(0,0)]]
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != 9:
                member_of_basin = False
                for outer in basins:
                    if (i,j) not in outer:
                        if (i-1,j) in outer:
                            outer.append((i,j))
                            member_of_basin = True
                        elif (i+1,j) in outer:
                            outer.append((i,j))
                            member_of_basin = True
                        elif (i,j-1) in outer:
                            outer.append((i,j))
                            member_of_basin = True
                        elif (i,j+1) in outer:
                            outer.append((i,j))
                            member_of_basin = True
                if not member_of_basin:
                    basins.append([(i,j)])

    return basins

def clean_up_basins(field1):
    cleaned_field = [[(0,0)]]
    for i in range(len(field1)):
        append_flag = True
        for j in range(len(cleaned_field)):
            if list_overlap(cleaned_field[j],field1[i]):
                append_flag = False
                for element in field1[i]:
                    if element not in cleaned_field[j]:
                        cleaned_field[j].append(element)
        if append_flag:
            cleaned_field.append(field1[i])
    return cleaned_field

def list_overlap(lst1,lst2):
    overlap = False
    for item in lst1:
        if item in lst2:
            overlap = True
    for item in lst2:
        if item in lst1:
            overlap = True
    return overlap
            


with open("09/input.txt", "r") as file:
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

to_clean = find_basins(field)
list_of_basins = clean_up_basins(to_clean)

list_of_basins.sort(key=len, reverse=True)

answer = 1

for mult in range(3):
    answer = answer * len(list_of_basins[mult])
print(answer)