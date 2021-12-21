def convert_to_bin(hexCode):
    deci = int(hexCode, 16)
    unpadded = bin(deci)[2:]
    padding = ''
    if len(unpadded) % 4:
        padding = '0'*(4-len(unpadded) % 4)
    return padding + unpadded


def vers_type(binCode):
    v = int(binCode[0:3], 2)
    t = int(binCode[3:6], 2)
    return v, t

def operation(num_list, typ):
    if typ == 0:
        number = 0
        for num in num_list:
            number += num
    elif typ == 1:
        number = 1
        for num in num_list:
            number = number*num
    elif typ == 2:
        number = min(num_list)
    elif typ == 3:
        number = max(num_list)
    elif typ == 5:
        if num_list[0] > num_list[1]:
            number = 1
        else:
            number = 0
    elif typ == 6:
        if num_list[0] < num_list[1]:
            number = 1
        else:
            number = 0
    elif typ == 7:
        if num_list[0] == num_list[1]:
            number = 1
        else:
            number = 0
    return number

def type_0(binCode, v_acc):
    '''returns the sub-packets' string'''
    v, t = vers_type(binCode)
    length = int(binCode[7:22], 2)
    binCode2 = binCode[22:22+length]
    operands = []
    while len(binCode2) > 10:
        binCode2, v_acc, number = decode(binCode2, v_acc)
        operands.append(number)
    number = operation(operands, t)
    return binCode[22+length:], v_acc, number


def literal_decode(binCode, v_acc):
    '''returns the first valid literal and the rest of the code'''
    str1 = ''
    last = False
    i, j = 7, 11
    while not last:
        str1 = str1 + binCode[i:j]
        if binCode[i-1] == '0':
            last = True
        else:
            i += 5
            j += 5
    return binCode[j:], v_acc, int(str1,2)


def type_1(binCode, v_acc):
    n_pck = int(binCode[7:18], 2)
    binCode3 = binCode[18:]
    v, t = vers_type(binCode)
    operands = []
    for _ in range(n_pck):
        binCode3, v_acc, number = decode(binCode3, v_acc)
        operands.append(number)
    number = operation(operands, t)
    return binCode3, v_acc, number


with open("16/input.txt", "r") as file:
    code = file.read()


# extract down to literal packets, append them to list
offset = 0
binar_list = [convert_to_bin(code)]
sub_packets = []
binar = binar_list[0]
# vers_accum += v


def decode(binCode, v_acc):
    v, t = vers_type(binCode)
    v_acc += v
    if t == 4:
        binCode, v_acc, number = literal_decode(binCode, v_acc)
        return binCode, v_acc, number
    elif binCode[6] == '0':
        binCode, v_acc, number = type_0(binCode, v_acc)
        return binCode, v_acc, number
    else:
        binCode, v_acc, number = type_1(binCode, v_acc)
        return binCode, v_acc, number


v_acc = 0

while len(binar) > 10:
    binar, v_acc, number = decode(binar, v_acc)

print(number)