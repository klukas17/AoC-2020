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
        currW = [10, 1]

    for instruction in instructions:

        letter = instruction[0]
        value = instruction[1]

        if letter == "N":
            currW[1] += value

        elif letter == "S":
            currW[1] -= value

        elif letter == "E":
            currW[0] += value

        elif letter == "W":
            currW[0] -= value

        elif letter == "L":
            i0 = currW[0]
            i1 = currW[1]
            if value == 90:
                currW[0] = -1 * i1
                currW[1] = i0
            elif value == 180:
                currW[0] = -1 * i0
                currW[1] = -1 * i1
            elif value == 270:
                currW[0] = i1
                currW[1] = -1 * i0

        elif letter == "R":
            i0 = currW[0]
            i1 = currW[1]
            if value == 90:
                currW[0] = i1
                currW[1] = -1 * i0
            elif value == 180:
                currW[0] = -1 * i0
                currW[1] = -1 * i1
            elif value == 270:
                currW[0] = -1 * i1
                currW[1] = i0
    
        elif letter == "F":
            currX += value * currW[0]
            currY += value * currW[1]
        
    return abs(currX + currY)

print(task())