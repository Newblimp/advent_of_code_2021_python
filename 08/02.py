def similarity(str1, ref):
    similarity_score = 0
    for c in ref:
        if c in str1:
            similarity_score += 1
    return similarity_score

def is_same(str1, str2):
    for c in str1:
        if c not in str2:
            return False
    for c in str2:
        if c not in str1:
            return False
    return True

final_sum = 0
with open("08/input.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        output = []
        signal_pattern = []
        for digit in line.split('|')[1].split():
            output.append(digit)
        for digit in line.split('|')[0].split():
            signal_pattern.append(digit)

        translation = {}

        #assign known series to translation dictionary
        for series in signal_pattern:
            if len(series) == 2:
                translation[1] = series
            elif len(series) == 3:
                translation[7] = series
            elif len(series) == 4:
                translation[4] = series
            elif len(series) == 7:
                translation[8] = series

        for series in signal_pattern:
            if len(series) == 5:
                if similarity(series, translation[1]) == 2:
                    translation[3] = series
                elif similarity(series, translation[4]) == 3:
                    translation[5] = series
                else:
                    translation[2] = series
            elif len(series) == 6:
                if similarity(series, translation[1]) == 1:
                    translation[6] = series
                elif similarity(series, translation[4]) == 3:
                    translation[0] = series
                else:
                    translation[9] = series

        multiplier = 1000
        sum = 0

        for code in output:
            for i in range(10):
                if is_same(code, translation[i]):
                    sum += i * multiplier
                    multiplier = multiplier//10
        final_sum += sum
print(final_sum)