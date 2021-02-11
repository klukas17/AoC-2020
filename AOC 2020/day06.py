def part1():
    programInput = open("day06.txt", "r").readlines()
    programInput.append("\n")

    lines = [line.strip() for line in programInput]

    answers = set()
    answerCount = 0

    for line in lines:

        if line == '':
            answerCount += len(answers)
            answers = set()
            continue

        for letter in line:
            answers.add(letter)

    return answerCount

def part2():
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

print(part1())
print(part2())