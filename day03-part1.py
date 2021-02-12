def task():
    fileStr = open("day03.txt", "r").readlines()
    lines = [i.strip() for i in fileStr]
    treesEncountered = 0
    currPosition = 0
    for line in lines[1:]:
        currPosition += 3
        currPosition %= len(line)
        if line[currPosition] == '#':
            treesEncountered += 1
    return treesEncountered

print(task())