def task():
    lines = []
    with open("day25.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    cardKey = int(lines[0])
    doorKey = int(lines[1])

    initialSubject = 1
    subject = 7
    modulo = 20201227

    cardLoop = 0
    initialSubject = 1

    while initialSubject != cardKey:
        cardLoop += 1
        initialSubject = (initialSubject * subject) % modulo

    doorLoop = 0
    initialSubject = 1

    while initialSubject != doorKey:
        doorLoop += 1
        initialSubject = (initialSubject * subject) % modulo

    result = 1
    for i in range(cardLoop):
        result = (result * doorKey) % modulo

    return result

print(task())