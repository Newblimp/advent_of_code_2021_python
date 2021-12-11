round = 0
square = 0
curly = 0
trig = 0

points = 0

with open("10/input.txt","r") as file:
    brackets = file.readlines()
    for line in brackets:
        str = []
        error_found = False
        for c in line:
            if not error_found:
                if c == '(':
                    str.append(c)
                elif c == '[':
                    str.append(c)
                elif c == '{':
                    str.append(c)
                elif c == '<':
                    str.append(c)
                elif c == ')':
                    if '(' == str[-1]:
                        str.pop(-1)
                    else:
                        points += 3
                        error_found = True
                elif c == ']':
                    if '[' == str[-1]:
                        str.pop(-1)
                    else:
                        points += 57
                        error_found = True
                elif c == '}':
                    if '{' == str[-1]:
                        str.pop(-1)
                    else:
                        points += 1197
                        error_found = True
                elif c == '>':
                    if '<' == str[-1]:
                        str.pop(-1)
                    else:
                        points += 25137
                        error_found = True



print(points)