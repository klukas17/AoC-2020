class MemoryLocation():

    MASK = 1
    COMMAND = 2

    def __init__(self, address, value):
        self.address = address
        self.value = value

def parseString(text):
    value = 0
    power = -1
    text = text[::-1]
    for c in text:
        power += 1
        if c == "1":
            value += pow(2, power)
    return value

def createString(num):
    text = ""
    while num != 0:
        char = num % 2
        num = num // 2
        text += str(char)
    while len(text) != 36:
        text += "0"
    text = text[::-1]
    return text

def calculateAdresses(address, mask):
    address = createString(address)
    realAddress = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            realAddress += "X"
        elif mask[i] == "0":
            realAddress += address[i]
        elif mask[i] == "1":
            realAddress += "1"
    addresses = [realAddress]
    Xs = [i for i in range(len(realAddress)) if realAddress[i] == "X"]
    for X in Xs:
        zeros = []
        ones = []
        for address in addresses:
            address = address[:X] + "0" + address[X+1:]
            zeros.append(address)
            address = address[:X] + "1" + address[X+1:]
            ones.append(address)
        addresses = zeros + ones
    addresses = [parseString(address) for address in addresses]
    return addresses

def task():
    inputText = open("day14.txt", "r").readlines()
    for i in range(len(inputText)):
        inputText[i] = inputText[i].strip()

    commands = []
    
    memoryLocations = []
    mask = None

    for line in inputText:
        if line[:3] == "mem":
            arr = line.split(" = ")
            arr[0] = arr[0][4:len(arr[0])-1]
            command = MemoryLocation.COMMAND, int(arr[0]), int(arr[1])
            commands.append(command)
        
        elif line[:3] == "mas":
            arr = line.split(" = ")
            mask = arr[1]
            command = MemoryLocation.MASK, mask
            commands.append(command)

    for command in commands:

        if command[0] == MemoryLocation.MASK:
            mask = command[1] 
            
        elif command[0] == MemoryLocation.COMMAND:
           addresses = calculateAdresses(command[1], mask)
           value = command[2]
           for address in addresses:
                memoryLocation = None
                for location in memoryLocations:
                   if location.address == address:
                       memoryLocation = location
                       break
                if memoryLocation:
                    memoryLocation.value = value
                else:
                    memoryLocations.append(MemoryLocation(address, value))

    sum = 0
    for location in memoryLocations:
        sum += location.value
        
    return sum
            
print(task())