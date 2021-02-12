def task():
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

print(task())