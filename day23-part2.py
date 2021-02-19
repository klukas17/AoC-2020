class Node():
    def __init__(self, cup):
        self.cup = cup
        self.next = None
        self.prev = None

def task():
    with open("day23.txt") as f:
        line = f.read()

    cupList = list(line)
    cupList = [int(cup) for cup in cupList]

    for i in range(len(cupList) + 1, 1000000 + 1):
        cupList.append(i)

    smallestCup = 1
    largestCup = 1000000

    cups = {}

    flag = True
    prev = None
    for cup in cupList:
        
        newCup = Node(cup)
        cups[cup] = newCup

        if flag:
            flag = False
            first = newCup

        if prev:
            prev.next = newCup
            newCup.prev = prev

        prev = newCup

    cups[1000000].next = first
    first.prev = cups[1000000]

    move = 0
    curr = cups[cupList[0]]

    while move < 10000000:

        move += 1

        cup1 = curr.next
        curr.next = cup1.next
        cup1.prev = cup1.next = None

        cup2 = curr.next
        curr.next = cup2.next
        cup2.prev = cup2.next = None

        cup3 = curr.next
        curr.next = cup3.next
        cup3.prev = cup3.next = None

        cup1.next = cup2
        cup2.prev = cup1
        cup2.next = cup3
        cup3.prev = cup2

        unassigned = [cup1.cup, cup2.cup, cup3.cup]

        next = curr.cup - 1
        if next < smallestCup:
            next = largestCup
        if next not in unassigned:
            dest = cups[next]
        else:
            while next in unassigned:
                next -= 1
                if next < smallestCup:
                    next = largestCup
            dest = cups[next]

        placeholder = dest.next
        cup3.next = placeholder
        placeholder.prev = cup3
        dest.next = cup1
        cup1.prev = dest

        curr = curr.next

    curr = cups[1]
    mul = curr.next.cup * curr.next.next.cup

    return mul

print(task())