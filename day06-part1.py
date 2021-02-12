def task():
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

print(task())