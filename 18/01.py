def add(str1, str2):
    str3 = '[' + str1.strip() + ',' + str2.strip() + ']'
    return str3


def reduce(str):
    reduced = False
    while not reduced:
        str, exploded = explode(str)
        if not exploded:
            str, has_split = split(str)
            if not has_split:
                reduced = True
    
    return str


def explode(str_in):
    brackets = 0
    str_out = ''
    exploded = False
    ante_digit_pos = 0
    post_digit_pos = 0

    # find explosion position
    for i in range(len(str_in)):
        if str_in[i] == '[':
            brackets += 1
        elif str_in[i] == ']':
            brackets -= 1
        if brackets == 5 and not exploded:
            expl_pos = i
            exploded = True

    if exploded:
        # digit before expl
        for i in range(expl_pos):
            if str_in[i] not in ['[', ']', ',']:
                ante_digit_pos = i

        # digit after expl
        for i in range(len(str_in)-1, expl_pos+4, -1):
            if str_in[i] not in ['[', ']', ',']:
                post_digit_pos = i

        if ante_digit_pos != 0:
            str_ante = str_in[0:ante_digit_pos] + str(int(str_in[ante_digit_pos]) + int(
                str_in[expl_pos+1])) + str_in[ante_digit_pos+1:expl_pos]
        else:
            str_ante = str_in[0:expl_pos]

        if post_digit_pos != 0:
            print(str_in[expl_pos:expl_pos+3])
            str_post = str_in[expl_pos+5:post_digit_pos] + str(int(str_in[post_digit_pos]) + int(
                str_in[expl_pos+3])) + str_in[post_digit_pos+1:]
        else:
            str_post = str_in[expl_pos+5:]

        str_out = str_ante + '0' + str_post
    else:
        str_out = str_in
    return str_out, exploded


def split(str_in):
    punctuation = ['[', ']', ',']
    split_found = False
    split_pos = 0
    for i in range(len(str_in)-1):
        if str_in[i] not in punctuation:
            if str_in[i+1] not in punctuation and not split_found:
                split_found = True
                split_pos = i
                split_num = int(str_in[i:i+2])
                if split_num % 2 == 0:
                    split_str = '[' + str(split_num//2) + \
                        ',' + str(split_num//2) + ']'
                else:
                    split_str = '[' + str(split_num//2) + \
                        ',' + str((split_num//2) + 1) + ']'
    if split_found:
        str_out = str_in[:split_pos] + split_str + str_in[split_pos+2:]
    else:
        str_out = str_in
    return str_out, split_found

with open('18/test.txt', 'r') as file:
    lines = file.readlines()

line =  lines[0]
for i in range(1, len(lines)):
    line = add(line, lines[i])
    line = reduce(line)
