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

        x = x / 2
        y = y * (3 ** 0.5)/2
            
        if (x,y) in tileMap:
            if tileMap[(x,y)] == 1:
                tileMap[(x,y)] = 0
            else:
                tileMap[(x,y)] = 1

        else:
            tileMap[(x,y)] = 1

    count = 0
    for tile in tileMap:
        if tileMap[tile] == 1:
            count += 1

    return count

print(task())