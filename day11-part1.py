class Position():

    def __init__(self, char):
        self.char = char
        self.neighbours = []

    def __str__(self):
        neighboursList = " -> "
        for neighbour in self.neighbours:
            neighboursList += neighbour.char + ", "
        neighboursList = neighboursList[:len(neighboursList)-2]
        return self.char + neighboursList

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

def task():

    global allPositions
    
    seatMap = open("day11.txt", "r").readlines()
    
    for i in range(len(seatMap)):
        seatMap[i] = seatMap[i].strip()

    allPositions = []

    for i in range(len(seatMap[0])):
        row = []
        for j in range(len(seatMap)):
            position = Position(seatMap[i][j])
            row.append(position)
        allPositions.append(row)

        x = len(seatMap[0])
        y = len(seatMap)

    for i in range(len(allPositions[0])):
        for j in range(len(allPositions)):

            curr = allPositions[i][j]

            if i - 1 >= 0 and j - 1 >= 0:
                curr.addNeighbour(allPositions[i-1][j-1])

            if i - 1 >= 0:
                curr.addNeighbour(allPositions[i-1][j])

            if i - 1 >= 0 and j + 1 <= y - 1:
                curr.addNeighbour(allPositions[i-1][j+1])
            
            if j - 1 >= 0:
                curr.addNeighbour(allPositions[i][j-1])
            
            if j + 1 <= y - 1:
                curr.addNeighbour(allPositions[i][j+1])

            if i + 1 <= x - 1 and j - 1 >= 0:
                curr.addNeighbour(allPositions[i+1][j-1])

            if i + 1 <= x - 1:
                curr.addNeighbour(allPositions[i+1][j])

            if i + 1 <= x - 1 and j + 1 <= y - 1:
                curr.addNeighbour(allPositions[i+1][j+1])

    change = True

    while change:
        change = simulate()

    occupied = 0

    for i in range(len(allPositions[0])):
        for j in range(len(allPositions)):
            if allPositions[i][j].char == "#":
                occupied += 1

    return occupied
    
def simulate():
    global allPositions
    
    seatsToBeFlipped = []

    for i in range(len(allPositions[0])):

        for j in range(len(allPositions)):

            empty = 0
            occupied = 0

            curr = allPositions[i][j]

            if curr.char == ".":
                continue

            for neighbour in curr.neighbours:
                if neighbour.char == "L":
                    empty += 1
                elif neighbour.char == "#":
                    occupied += 1
            
            if curr.char == "L" and occupied == 0:
                seatsToBeFlipped.append(curr)

            elif curr.char == "#" and occupied >= 4:
                seatsToBeFlipped.append(curr)

    for seat in seatsToBeFlipped:
        if seat.char == "L":
            seat.char = "#"
        elif seat.char == "#":
            seat.char = "L"

    return len(seatsToBeFlipped) != 0

print(task())