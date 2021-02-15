def task():
    inputText = open("day17.txt", "r").readlines()

    lines = [line.strip() for line in inputText]

    turns = 6

    cubes = []
    
    xMin = 0
    xMax = len(lines) - 1
    yMin = 0
    yMax = len(lines[0]) - 1
    zMin = 0
    zMax = 0

    xMin -= turns + 2
    xMax += turns + 2
    yMin -= turns + 2
    yMax += turns + 2
    zMin -= turns + 2
    zMax += turns + 2

    cubes = []
    for i in range(xMin, xMax + 1):
        x = []
        for j in range(yMin, yMax + 1):
            y = []
            for k in range(zMin, zMax + 1):
                y.append(".")
            x.append(y)
        cubes.append(x)

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            cubes[i+turns+1][j+turns+1][turns+1] = lines[i][j]

    
    turn = 0
    while turn != turns:

        turn += 1

        toBeSwitched = []
        for i in range(xMin, xMax + 1):
            for j in range(yMin, yMax + 1):
                for k in range(zMin, zMax + 1):
                    active = 0
                    for x in range(i-1, i+2):
                        for y in range(j-1, j+2):
                            for z in range(k-1, k+2):
                                if (x,y,z) != (i,j,k) and cubes[x][y][z] == "#":
                                    active += 1
                    if cubes[i][j][k] == "#":
                        if active != 2 and active != 3:
                            toBeSwitched.append((i,j,k))
                    else:
                        if active == 3:
                            toBeSwitched.append((i,j,k))

        for el in toBeSwitched:
            cube = cubes[el[0]][el[1]][el[2]]
            if cube == ".":
                cubes[el[0]][el[1]][el[2]] = "#"
            else:
                cubes[el[0]][el[1]][el[2]] = "."

    active = 0
    for i in range(xMin, xMax + 1):
        for j in range(yMin, yMax + 1):
            for k in range(zMin, zMax + 1):
                if cubes[i][j][k] == "#":
                    active += 1
    
    return active

print(task())