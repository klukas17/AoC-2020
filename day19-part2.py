global rules

def task():

    global rules

    lines = []
    with open("test.txt") as f:
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
    for i in range(43):
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

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    valid = 0

    for message in messages:
        
        if validZero(message):
            valid += 1

    return valid

def validZero(message):

    for limit in range(1, len(message)):
        try:
            if validEight(message[:limit]) and validEleven(message[limit:]):
                return True
        except:
            pass
    
    return False

def validEight(message):

    if len(message) == 0:
        return True
    
    for limit in range(len(message), 0, -1):
        try:
            if validSimple(message[:limit], 42) == len(message[:limit]) and validEight(message[limit:]):
                return True
        except:
            pass

    return False

def validEleven(message):

    if len(message) == 0:
        return True
    
    for limit1 in range(1, len(message)):
        for limit2 in range(limit1, len(message)):
            try:
                if validSimple(message[:limit1], 42) == len(message[:limit1]) and validEleven(message[limit1:limit2]) and validSimple(message[limit2:], 31) == len(message[limit2:]):
                    return True
            except:
                pass

    return False

def validSimple(message, rule):

    global rules
    
    if len(message) == 0:
        return 0

    if isinstance(rules[rule][0], str):
        if message[index] == rules[rule][0]:
            return index + 1
        else:
            raise

    else:

        startIndex = index
        for arr in rules[rule]:
            index = startIndex
            try:
                for el in arr:
                    index = isValid(message, el, index)
                return index
            except:
                continue
        raise

print(task())