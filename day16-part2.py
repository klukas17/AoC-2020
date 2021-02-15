global ruleCount

class Rule():

    global ruleCount

    def __init__(self, index, intervals):
        self.index = index
        self.interval = []
        for interval in intervals:
            for i in range(int(interval[0]), int(interval[1]) + 1):
                self.interval.append(i)
        self.potentialFields = []
        for i in range(ruleCount):
            self.potentialFields.append(i)

def task():

    global ruleCount

    fileInput = open("day16.txt", "r").readlines()
    lines = [line.strip() for line in fileInput]

    rules = []
    myTicket = ""
    tickets = []

    count = 1
    arr1 = []
    arr2 = []
    arr3 = []

    for line in lines:
        if line == "":
            count += 1
        else:
            if count == 1:
                arr1.append(line)
            elif count == 2:
                arr2.append(line)
            else:
                arr3.append(line)

    myTicket = [int(el) for el in arr2[1].split(",")]
    departureFields = []
    for i in range(len(arr1)):
        el = arr1[i].split(" ")
        if el[0] == "departure":
            departureFields.append(i)

    ruleCount = len(arr1)

    rules = []

    for i in range(len(arr1)):
        line = arr1[i]
        line = line.split(": ")
        line = line[1]
        line = line.split(" or ")
        rule = Rule(i, [el.split("-") for el in line])
        rules.append(rule)

    tickets = []
    for line in arr3[1:]:
        ticket = [int(el) for el in line.split(",")]
        tickets.append(ticket)

    validTickets = []

    for ticket in tickets:
        flag = True
        for num in ticket:
            fieldFlag = False
            for rule in rules:
                if num in rule.interval:
                    fieldFlag = True
            if not fieldFlag:
                flag = False
        if flag:
            validTickets.append(ticket)
    
    for i in range(len(rules)):
        column = [ticket[i] for ticket in validTickets]
        for rule in rules:
            for el in column:
                if el not in rule.interval:
                    rule.potentialFields.remove(i)

    ruleList = rules
    connections = []
    for i in range(len(rules)):
        connections.append(None)
    
    while len(ruleList) != 0:
        for rule in ruleList:
            if len(rule.potentialFields) == 1:
                el = rule.potentialFields[0]
                connections[rule.index] = el
                ruleList.remove(rule)
                for rule in ruleList:
                    if el in rule.potentialFields:
                        rule.potentialFields.remove(el)
                continue

    result = 1
    for el in departureFields:
        result *= myTicket[connections[el]]

    return result

print(task())