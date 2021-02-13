import math

class Bus():
    def __init__(self, ID, wait):
        self.ID = ID
        self.wait = wait

def task():
    inputText = open("day13.txt", "r").readlines()
    timestamp = inputText[0]
    buses = inputText[1]
    timestamp = timestamp.strip()
    buses = buses.strip()
    timestamp = int(timestamp)
    IDs = []
    buses = buses.split(",")
    for bus in buses:
        if bus != "x":
            IDs.append(int(bus))

    allBuses = []

    for ID in IDs:
        wait = ID - timestamp % ID if timestamp % ID != 0 else 0
        bus = Bus(ID, wait)
        allBuses.append(bus)

    ID = 0
    wait = -1
    for bus in allBuses:
        if wait == -1 or bus.wait < wait or (bus.wait == wait and ID > bus.ID):
            ID = bus.ID
            wait = bus.wait

    return ID * wait

print(task())
