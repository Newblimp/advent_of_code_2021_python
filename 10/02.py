round = 0
square = 0
curly = 0
trig = 0

points = 0

incomplete_lines = []

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
                        error_found = True
                elif c == ']':
                    if '[' == str[-1]:
                        str.pop(-1)
                    else:
                        error_found = True
                elif c == '}':
                    if '{' == str[-1]:
                        str.pop(-1)
                    else:
                        error_found = True
                elif c == '>':
                    if '<' == str[-1]:
                        str.pop(-1)
                    else:
                        error_found = True
        if not error_found:
            incomplete_lines.append(str)


scores = [0]*len(incomplete_lines)
tracker = 0

for line in incomplete_lines:
    for i in range(1,len(line)+1):
        scores[tracker] = scores[tracker]*5
        if line[-i] == '(':
            scores[tracker] += 1
        elif line[-i] == '[':
            scores[tracker] += 2
        elif line[-i] == '{':
            scores[tracker] += 3
        elif line[-i] == '<':
            scores[tracker] += 4
    tracker += 1
    

scores.sort()
middle = len(scores)//2
print(scores[middle])