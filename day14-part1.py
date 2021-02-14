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

def calculateValue(value, mask):
    value = createString(value)
    retValue = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            retValue += value[i]
        else:
            retValue += mask[i]
    return parseString(retValue)

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
            value = calculateValue(command[2], mask)
            memoryLocation = None
            for location in memoryLocations:
                if location.address == command[1]:
                    memoryLocation = location
                    break
            if memoryLocation:
                memoryLocation.value = value
            else:
                memoryLocations.append(MemoryLocation(command[1], value))

    sum = 0
    for location in memoryLocations:
        sum += location.value
        
    return sum
            
print(task())