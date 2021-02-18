global rules
global validMessages

def task():

    global rules
    global validMessages

    lines = []
    with open("day19.txt") as f:
        lines = [l.strip() for l in f.readlines()]

    ruleList = []
    messages = []

    flag = True
    for line in lines:

        if line == "":
            flag = False
            continue

        if flag:
            ruleList.append((int(line.split(": ")[0]),line.split(": ")[1].split(" | ")))

        else:
            messages.append(line)

    rules = []
    for i in range(len(ruleList)):
        rules.append(None)

    for rule in ruleList:

        arr = []
        for el in rule[1]:

            flag = False
            try:
                a = int(el[0])
                flag = True
            except:
                pass

            if flag:
                arr.append([int(n) for n in el.split(" ")])
            else:
                arr.append(el[1:len(el)-1])

        rules[rule[0]] = arr

    validMessages = []
    for i in range(len(rules)):
        validMessages.append(None)

    for i in range(len(rules)):
        validMessages[i] = computeMessages(i)

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    valid = 0
    count = 0
    complete = len(messages)

    print(str(count) + "/" + str(complete))
    
    for message in messages:

        if validZero(message):
            valid += 1

        count += 1
        print(str(count) + "/" + str(complete))

    return valid

def computeMessages(rule):

    global rules

    retVal = set()
    if isinstance(rules[rule][0], str):
        retVal.add(rules[rule][0])
        return retVal 

    for ruleSet in rules[rule]:

        if len(ruleSet) == 1:
            s = computeMessages(ruleSet[0])

        else:
            s1 = computeMessages(ruleSet[0])
            s2 = computeMessages(ruleSet[1])

            s = set()

            l1 = list(s1)
            l2 = list(s2)
            
            for i in range(len(l1)):
                for j in range(len(l2)):
                    mg = l1[i] + l2[j]
                    s.add(mg)
    
        retVal = retVal.union(s)

    return retVal

def validZero(message):

    global validMessages

    for limit in range(1, len(message)):
        if validEight(message[:limit]) and validEleven(message[limit:]):
            return True

    return False

def validEight(message):

    global validMessages

    if len(message) == 0:
        return True
    
    for limit in range(len(message), 0, -1):
        if message[:limit] in validMessages[42] and validEight(message[limit:]):
            return True

    return False

def validEleven(message):

    global validMessages

    if len(message) == 0:
        return True

    for limit1 in range(1, len(message)):
        for limit2 in range(limit1, len(message)):
            if message[:limit1] in validMessages[42] and validEleven(message[limit1:limit2]) and message[limit2:] in validMessages[31]:
                return True

    return False

print(task())