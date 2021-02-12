def task():
    programInput = open("day05.txt", "r").readlines()
    lines = [line.strip() for line in programInput]

    maxID = 0

    for line in lines:

        rowText = line[:7]
        columnText = line[7:]

        rowText = rowText[::-1]
        columnText = columnText[::-1]

        rowNumber = 0
        columnNumber = 0

        rowPower = 0
        columnPower = 0

        for letter in rowText:
            if letter == "F":
                rowPower += 1
            elif letter == "B":
                rowNumber += pow(2, rowPower)
                rowPower += 1

        for letter in columnText:
            if letter == "L":
                columnPower += 1
            elif letter == "R":
                columnNumber += pow(2, columnPower)
                columnPower += 1

        seatID = rowNumber * 8 + columnNumber
        if seatID > maxID:
            maxID = seatID
    
    return maxID

print(task())