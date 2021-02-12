def task():
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

print(task())