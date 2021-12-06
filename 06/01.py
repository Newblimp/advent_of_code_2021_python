numbers = []
with open("06/input.txt", "r") as file:
    list = file.read().split(',')
    for _ in range(len(list)):
        numbers.append(int(list[_]))

days = 80
print(len(numbers))

for day in range(days):
    for i in range(len(numbers)):
        if numbers[i] > 0:
            numbers[i] -= 1
        else:
            numbers[i] = 6
            numbers.append(8)

print(len(numbers))