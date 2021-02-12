def task():
    number = 1
    number *= traverse(1, 1)
    number *= traverse(3, 1)
    number *= traverse(5, 1)
    number *= traverse(7, 1)
    number *= traverse(1, 2)
    return number

def traverse(right, down):
    fileStr = open("day03.txt", "r").readlines()
    lines = [i.strip() for i in fileStr]
    linesVisited = [lines[i] for i in range(1, len(lines)) if i % down == 0]
    currPosition = 0
    treesEncountered = 0
    for line in linesVisited:
        currPosition += right
        currPosition %= len(line)
        if line[currPosition] == '#':
            treesEncountered += 1
    return treesEncountered

print(task())