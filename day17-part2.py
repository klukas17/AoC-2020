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
    wMin = 0
    wMax = 0

    xMin -= turns + 2
    xMax += turns + 2
    yMin -= turns + 2
    yMax += turns + 2
    zMin -= turns + 2
    zMax += turns + 2
    wMin -= turns + 2
    wMax += turns + 2

    cubes = []
    for i in range(xMin, xMax + 1):
        x = []
        for j in range(yMin, yMax + 1):
            y = []
            for k in range(zMin, zMax + 1):
                z = []
                for l in range(wMin, wMax + 1):
                    z.append(".")
                y.append(z)
            x.append(y)
        cubes.append(x)

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            cubes[i+turns+1][j+turns+1][turns+1][turns+1] = lines[i][j]

    turn = 0
    while turn != turns:

        turn += 1

        toBeSwitched = []
        for i in range(xMin, xMax + 1):
            for j in range(yMin, yMax + 1):
                for k in range(zMin, zMax + 1):
                    for l in range(wMin, wMax + 1):
                        active = 0
                        for x in [i-1,i,i+1]:
                            for y in [j-1,j,j+1]:
                                for z in [k-1,k,k+1]:
                                    for w in [l-1,l,l+1]:
                                        if (x,y,z,w) != (i,j,k,l) and cubes[x][y][z][w] == "#":
                                            active += 1
                        if cubes[i][j][k][l] == "#":
                            if active != 2 and active != 3:
                                toBeSwitched.append((i,j,k,l))
                        else:
                            if active == 3:
                                toBeSwitched.append((i,j,k,l))

        for el in toBeSwitched:
            if cubes[el[0]][el[1]][el[2]][el[3]] == ".":
                cubes[el[0]][el[1]][el[2]][el[3]] = "#"
            else:
                cubes[el[0]][el[1]][el[2]][el[3]] = "."

    active = 0
    for i in range(xMin, xMax + 1):
        for j in range(yMin, yMax + 1):
            for k in range(zMin, zMax + 1):
                for l in range(wMin, wMax + 1):
                    if cubes[i][j][k][l] == "#":
                        active += 1
    
    return active

print(task())