def part1():
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

def part2():
    number = 1
    number *= part2_traverse(1, 1)
    number *= part2_traverse(3, 1)
    number *= part2_traverse(5, 1)
    number *= part2_traverse(7, 1)
    number *= part2_traverse(1, 2)
    return number

def part2_traverse(right, down):
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

print(part1())
print(part2())