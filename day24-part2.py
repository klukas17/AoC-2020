def task():
    lines = []
    with open("day24.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        
    tiles = []
    for line in lines:
        row = []
        flag = False
        for i in range(len(line)):

            if flag:
                flag = False
                continue

            if line[i] in ["e", "w"]:
                row.append(line[i])
            
            else:
                row.append(line[i] + line[i+1])
                flag = True

        tiles.append(row)

    tileMap = {}
    
    for tile in tiles:
        x = 0
        y = 0

        for el in tile:
            if el == "ne":
                x += 1
                y += 1
            elif el == "sw":
                x -= 1
                y -= 1
            elif el == "e":
                x += 2
            elif el == "w":
                x -= 2
            elif el == "se":
                x += 1
                y -= 1
            elif el == "nw":
                x -= 1
                y += 1

        if (x,y) in tileMap:
            if tileMap[(x,y)] == 1:
                tileMap[(x,y)] = 0
            else:
                tileMap[(x,y)] = 1

        else:
            tileMap[(x,y)] = 1

    vectors = [(2,0), (-2, 0), (1,-1), (1, 1), (-1, 1), (-1,-1)]
    move = 0

    while move < 100:
        
        move += 1

        toBeMade = set()

        for tile in tileMap:

            for vector in vectors:
                cord = (tile[0] + vector[0], tile[1] + vector[1])

                if cord not in tileMap:
                    toBeMade.add(cord)

        for cord in toBeMade:
            tileMap[cord] = 0
    
        toBeFlipped = []

        for tile in tileMap:
            
            black = 0

            for vector in vectors:
                cord = (tile[0] + vector[0], tile[1] + vector[1])
                if cord in tileMap:
                    if tileMap[cord] == 1:
                        black += 1

            if tileMap[tile] == 1 and black not in [1, 2]:
                toBeFlipped.append(tile)

            elif tileMap[tile] == 0 and black == 2:
                toBeFlipped.append(tile)

        for tile in toBeFlipped:
            if tileMap[tile] == 1:
                tileMap[tile] = 0
            else:
                tileMap[tile] = 1

    black = 0
    for tile in tileMap:
        if tileMap[tile] == 1:
            black += 1

    return black

print(task())