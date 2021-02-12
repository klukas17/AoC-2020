def task():
    fileStr = open("day01.txt", "r").readlines()
    fileInt = [int(i) for i in fileStr]
    for i in fileInt:
        for j in fileInt:
            for k in fileInt:
                if i + j + k == 2020:
                    return i * j * k

print(task())