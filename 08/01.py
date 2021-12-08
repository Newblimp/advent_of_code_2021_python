output = []
with open("08/input.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        for digit in line.split('|')[1].split():
            output.append(digit)

code_length = {}
for code in output:
    if len(code) not in code_length:
        code_length[len(code)] = 0
    code_length[len(code)] += 1
   
sum = code_length[2] + code_length[4] + code_length[3] + code_length[7]

print(sum)