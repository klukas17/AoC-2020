class Tile():

    def __init__(self, index):
        self.index = index
        self.tiles = None
        self.matrix = None
        self.edges = None
    
    def createMatrix(self):
        self.matrix = []
        for line in self.tiles:
            row = []
            for c in line:
                row.append(c)
            self.matrix.append(row)

    def createEdges(self):

        edge1 = self.tiles[0]
        edge2 = ''.join([l[len(self.tiles)-1] for l in self.tiles])
        edge3 = self.tiles[len(self.tiles)-1]
        edge4 = ''.join([l[0] for l in self.tiles])

        self.edges = (edge1, edge2, edge3, edge4)

def task():
    lines = []
    with open("day20.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    lines.append("")

    rowLength = len(lines[1])

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
        tile.createEdges()

    edges = []
    for tile in tiles:
        for edge in tile.edges:
            edges.append(edge)

    edgeMatchings = {}

    for i in range(len(edges)):
        flag = True
        for j in range(len(edges)):
            if i == j:
                continue
            if edges[i] == edges[j] or edges[i] == edges[j][::-1]:
                flag = False
                edgeMatchings[i] = j
                edgeMatchings[j] = i
        if flag:
            edgeMatchings[i] = None

    corners = []
    counter = 0
    for i in range(len(edgeMatchings)):
        if i % 4 == 0:
            counter = 0
        if edgeMatchings[i] == None:
            counter += 1
        if counter == 2:
            corners.append(int(i / 4))
            counter = 0
    
    mul = 1
    for corner in corners:
        mul *= tiles[corner].index

    return mul

print(task())