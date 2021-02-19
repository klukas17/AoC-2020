def task():
    with open("day23.txt") as f:
        line = f.read()

    cups = list(line)
    cups = [int(cup) for cup in cups]

    cupsCopy = cups.copy()
    cupsCopy.sort()

    mincup = cupsCopy[0]
    maxCup = cupsCopy[-1]

    move = 0
    curr = cups[0]

    while move < 100:
        move += 1
        cup1 = cups.pop(1)
        cup2 = cups.pop(1)
        cup3 = cups.pop(1)

        if curr - 1 in cups:
            dest = curr - 1

        else:
            next = curr - 1
            while next not in cups:
                next -= 1
                if next < mincup:
                    next = maxCup
            dest = next

        cups.insert(cups.index(dest) + 1, cup3)
        cups.insert(cups.index(dest) + 1, cup2)
        cups.insert(cups.index(dest) + 1, cup1)

        help = cups[0]
        for i in range(len(cups) - 1):
            cups[i] = cups[i+1]
        cups[len(cups)-1] = help
        
        curr = cups[0]
        
    while cups[0] != 1:
        help = cups[0]
        for i in range(len(cups) - 1):
            cups[i] = cups[i+1]
        cups[len(cups)-1] = help

    result = ""
    for i in range(1, len(cups)):
        result += str(cups[i])

    return result

print(task())