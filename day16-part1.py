def task():
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

    rules = []

    for line in arr1:
        line = line.split(": ")
        line = line[1]
        line = line.split(" or ")
        rule = []
        for el in line:
            numRange = el.split("-")
            rule.append((int(numRange[0]), int(numRange[1])))
        rules.append(rule)

    tickets = []
    for line in arr3[1:]:
        ticket = [int(el) for el in line.split(",")]
        tickets.append(ticket)

    error = 0

    for ticket in tickets:
        for num in ticket:
            flag = False
            for rule in rules:
                for numRange in rule:
                    if numRange[0] <= num <= numRange[1]:
                        flag = True
            if not flag:
                error += num

    return error

print(task())