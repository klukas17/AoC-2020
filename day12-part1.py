def task():
    inputText = open("day12.txt", "r").readlines()

    for i in range(len(inputText)):
        inputText[i] = inputText[i].strip()

    instructions = []

    for line in inputText:

        letter = line[0]
        number = int(line[1:])
        instructions.append((letter,number))

    currX = 0
    currY = 0
    currD = (1, 0)

    for instruction in instructions:

        letter = instruction[0]
        value = instruction[1]

        if letter == "N":
            currY += value

        elif letter == "S":
            currY -= value

        elif letter == "E":
            currX += value

        elif letter == "W":
            currX -= value

        elif letter == "L":
            if value == 90:
                newX = -1 * currD[1]
                newY = currD[0]
                currD = (newX, newY)
            elif value == 180:
                newX = -1 * currD[0]
                newY = -1 * currD[1]
                currD = (newX, newY)
            elif value == 270:
                newX = currD[1]
                newY = -1 * currD[0]
                currD = (newX, newY)

        elif letter == "R":
            if value == 90:
                newX = currD[1]
                newY = -1 * currD[0]
                currD = (newX, newY)
            elif value == 180:
                newX = -1 * currD[0]
                newY = -1 * currD[1]
                currD = (newX, newY)
            elif value == 270:
                newX = -1 * currD[1]
                newY = currD[0]
                currD = (newX, newY)
    
        elif letter == "F":
            dx = currD[0] * value
            dy = currD[1] * value
            currX += dx
            currY += dy
        
    return abs(currX + currY)

print(task())