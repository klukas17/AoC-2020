global rules

def task():

    global rules

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

    valid = 0

    for message in messages:
        try:
            matched = isValid(message, 0, 0)
            if matched == len(message):
                valid += 1
        except:
            pass

    return valid

def isValid(message, rule, index):

    global rules

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