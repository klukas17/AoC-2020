def task():
    fileStr = open("day01.txt", "r").readlines()
    fileInt = [int(i) for i in fileStr]
    for i in fileInt:
        for j in fileInt:
            if i + j == 2020:
                return i * j

print(task())