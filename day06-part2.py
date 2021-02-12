def task():
    programInput = open("day06.txt", "r").readlines()
    programInput.append("\n")

    lines = [line.strip() for line in programInput]

    answers = []
    answerCount = 0

    for line in lines:
        
        if line == '':
            finalSet = answers[0]
            for currSet in answers[1:]:
                finalSet = finalSet.intersection(currSet)

            answerCount += len(finalSet)
            answers = []
            continue

        newSet = set()
        for letter in line:
            newSet.add(letter)
        answers.append(newSet)

    return answerCount

print(task())