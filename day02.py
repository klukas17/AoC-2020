def part1():
    fileStr = open("day02.txt", "r").readlines()
    validPasswords = 0
    for i in fileStr:
        arr = i.split(" ")
        numRange = arr[0].split("-")
        minimal = int(numRange[0])
        maximal = int(numRange[1])
        letter = arr[1][0]
        text = arr[2]
        occurrences = 0
        for j in text:
            if j == letter:
                occurrences += 1
        if occurrences >= minimal and occurrences <= maximal:
            validPasswords += 1
    return validPasswords

def part2():
    fileStr = open("day02.txt", "r").readlines()
    validPasswords = 0
    for i in fileStr:
        arr = i.split(" ")
        numRange = arr[0].split("-")
        first = int(numRange[0])
        second = int(numRange[1])
        letter = arr[1][0]
        text = arr[2]
        flag1 = True if text[first - 1] == letter else False
        flag2 = True if text[second - 1] == letter else False
        if flag1 != flag2:
            validPasswords += 1
    return validPasswords

print(part1())
print(part2())