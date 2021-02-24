class Tile():

    def __init__(self, index):
        self.index = index
        self.matrix = None
        self.edges = None
        self.tiles = None
        self.neighbours = None
        self.dimension = None
    
    def createMatrix(self):
        self.matrix = []
        for line in self.tiles:
            row = []
            for c in line:
                row.append(c)
            self.matrix.append(row)
        self.dimension = len(self.tiles)

        self.adjustEdges()

    def adjustEdges(self):
        
        edge1 = self.tiles[0]
        edge2 = ''.join([l[len(self.tiles)-1] for l in self.tiles])
        edge3 = self.tiles[len(self.tiles)-1]
        edge4 = ''.join([l[0] for l in self.tiles])

        self.edges = (edge1, edge2, edge3, edge4)

    def rotateRight(self):
        matrix = []
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension - 1, -1, -1):
                row.append(self.matrix[j][i])
            matrix.append(row)
        self.matrix = matrix
        self.rotateRightAdjustEdges()

    def flipRows(self):
        
        for i in range(int(self.dimension/2)):
            help = self.matrix[i]
            self.matrix[i] = self.matrix[self.dimension-1-i]
            self.matrix[self.dimension-1-i] = help

        self.flipRowsAdjustEdges()

    def flipColumns(self):
        matrix = []
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension - 1, -1, -1):
                row.append(self.matrix[i][j])
            matrix.append(row)
        self.matrix = matrix
        self.flipColumnsAdjustEdges()

    def mergeEdgesAndNeighbours(self):
        edge1 = [self.edges[0], self.neighbours[0]]
        edge2 = [self.edges[1], self.neighbours[1]]
        edge3 = [self.edges[2], self.neighbours[2]]
        edge4 = [self.edges[3], self.neighbours[3]]
        self.edges = [edge1, edge2, edge3, edge4]

    def rotateRightAdjustEdges(self):
        newEdge0 = self.edges[3]
        newEdge1 = self.edges[0]
        newEdge2 = self.edges[1]
        newEdge3 = self.edges[2]
        self.edges = (newEdge0, newEdge1, newEdge2, newEdge3)

    def flipRowsAdjustEdges(self):
        newEdge0 = self.edges[2]
        newEdge1 = self.edges[1]
        newEdge2 = self.edges[0]
        newEdge3 = self.edges[3]
        self.edges = (newEdge0, newEdge1, newEdge2, newEdge3)

    def flipColumnsAdjustEdges(self):
        newEdge0 = self.edges[0]
        newEdge1 = self.edges[3]
        newEdge2 = self.edges[2]
        newEdge3 = self.edges[1]
        self.edges = (newEdge0, newEdge1, newEdge2, newEdge3)

    def getEdge1(self):
        edge = ""
        for el in self.matrix:
            edge += el[self.dimension-1]
        return edge

    def getEdge3(self):
        edge = ""
        for el in self.matrix:
            edge += el[0]
        return edge

def rotation(matrix):
    newMatrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix) - 1, -1, -1):
            row.append(matrix[j][i])
        newMatrix.append(row)
    matrix = newMatrix
    return matrix

def flip(matrix):
    for i in range(int(len(matrix)/2)):
        help = matrix[i]
        matrix[i] = matrix[len(matrix)-1-i]
        matrix[len(matrix)-1-i] = help
    return matrix

def printMatrix(matrix):
    retVal = ""
    count = 0
    count2 = 0
    for i in range(len(matrix)):
        count += 1
        row = ""
        for j in range(len(matrix)):
            count2 += 1
            row += matrix[i][j]
            if count2 % 10 == 0:
                row += "    "
        retVal += row + "\n"
        if count % 10 == 0:
            retVal += "\n"
    return retVal

def task():
    lines = []
    with open("day20.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    lines.append("")

    tiles = []
    tile = None
    arr = []

    for line in lines:
        if line == "":
            tile.tiles = arr
            arr = []
            tile = None
        elif line[0] == "T":
            tile = Tile(int(line.split(" ")[1][:len(line.split(" ")[1])-1]))
            tiles.append(tile)
        else:
            arr.append(line)

    for tile in tiles:
        tile.createMatrix()

    for i in range(len(tiles)):

        curr = tiles[i]
        neighbours = []

        for edge in curr.edges:

            neighbour = None

            for j in range(len(tiles)):

                if i == j:
                    continue

                sus = tiles[j]

                for edge2 in sus.edges:
                    if edge == edge2 or edge == edge2[::-1]:
                        neighbour = sus

            neighbours.append(neighbour)

        curr.neighbours = neighbours
    
    for curr in tiles:
        curr.mergeEdgesAndNeighbours()

    curr = None
    for tile in tiles:
        neigh = [neighbour for neighbour in tile.neighbours if neighbour]
        if len(neigh) == 2:
            if curr == None or curr.index > tile.index:
                curr = tile

    while True:
        if curr.edges[1][1] != None and curr.edges[2][1] != None:
            break
        curr.rotateRight()

    image = []
    for i in range(int(len(tiles) ** 0.5)):
        row = []
        for j in range(int(len(tiles) ** 0.5)):
            row.append(None)
        image.append(row)

    i = 0
    j = 0
    image[i][j] = curr
    rowStart = curr

    while curr.edges[1][1]:
        next = curr.edges[1][1]

        while curr.edges[1][0] != next.edges[3][0] and curr.edges[1][0] != next.edges[3][0][::-1]:
            next.rotateRight()

        if next.edges[2][1] == None:
            next.flipRows()

        j += 1
        image[i][j] = next
        curr = next

    i += 1
        
    for k in range(len(image)-1):
        j = 0
        
        curr = rowStart
        next = curr.edges[2][1]

        while curr.edges[2][0] != next.edges[0][0] and curr.edges[2][0] != next.edges[0][0][::-1]:
            next.rotateRight()

        if next.edges[1][1] == None:
            next.flipColumns()

        image[i][j] = next
        rowStart = curr
        curr = next

        while curr.edges[1][1]:
            next = curr.edges[1][1]

            while curr.edges[1][0] != next.edges[3][0] and curr.edges[1][0] != next.edges[3][0][::-1]:
                next.rotateRight()

            if next.getEdge3() != curr.getEdge1():
                next.flipRows()

            j += 1
            image[i][j] = next
            curr = next

        i += 1
        rowStart = rowStart.edges[2][1]

    picture = []

    for i in range(len(image)):
        for j in range(len(image[0][0].matrix)):
            row = []
            for k in range(len(image)):
                for l in range(len(image[0][0].matrix)):
                    row += image[i][k].matrix[j][l]
            picture.append(row)

    toBeRemoved = []
    for i in range(len(image)):
        toBeRemoved.append(10 * i)
        toBeRemoved.append(10 * i + 9)
    
    toBeRemoved = toBeRemoved[::-1]

    for el in toBeRemoved:
        picture.pop(el)

    for el in toBeRemoved:
        for line in picture:
            line.pop(el)

    pattern = [(18, 0), (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1), (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]
    patternRowLength = 20
    patternColumnLength = 3
    pictureDimension = len(picture)
    hashesInMonster = 15
    hashCount = 0
    for i in range(len(picture)):
        for j in range(len(picture)):
            if picture[i][j] == "#":
                hashCount += 1

    count = 0

    while True:

        count += 1

        found = 0
        foundCoordinates = []
        
        for i in range(pictureDimension-patternRowLength):
            for j in range(pictureDimension-patternColumnLength):
                flag = True
                for cord in pattern:
                    newCord = (cord[0] + i, cord[1] + j)
                    if picture[newCord[0]][newCord[1]] != "#" or newCord in foundCoordinates:
                        flag = False
                if flag:
                    found += 1
                    for cord in pattern:
                        foundCoordinates.append((cord[0]+i, cord[1]+j))
        
        if found != 0:
            return hashCount - hashesInMonster * found

        picture = rotation(picture)

        if count % 4 == 0:
            picture = flip(picture)

print(task())