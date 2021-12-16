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

def literal_decode(binCode, offs=0):
    '''returns the first valid literal and the rest of the code'''
    v, t = vers_type(binCode)
    # print(v)
    str1 = ''
    last = False
    i, j = 7+offs, 11+offs
    while not last:
        str1 = str1 + binCode[i:j]
        if binCode[i-1] == '0':
            last = True
        else:
            i += 5
            j += 5
    return int(str1, 2), binCode[j:]

with open("16/test.txt", "r") as file:
    code = file.read()

code = convert_to_bin(code)
