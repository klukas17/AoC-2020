def task():
    inputText = open("day10.txt", "r").readlines()
    for line in inputText:
        line.strip("\n")
    numbers = [int(line) for line in inputText]
    numbers.append(0)
    numbers.append(max(numbers)+3)
    numbers.sort()
    numbers = numbers[::-1]

    print(numbers)

    paths = []
    paths.append(1)

    for i in range(1, len(numbers)):

        if i == 1:
            paths.append(1)
            continue

        if i == 2:
            valid = 0
            if numbers[i-2] - numbers[i] <= 3:
                valid += paths[i-2]
            if numbers[i-1] - numbers[i] <= 3:
                valid += paths[i-1]
            paths.append(valid)
            continue

        valid = 0
        if numbers[i-3] - numbers[i] <= 3:
            valid += paths[i-3]
        if numbers[i-2] - numbers[i] <= 3:
            valid += paths[i-2]
        if numbers[i-1] - numbers[i] <= 3:
            valid += paths[i-1]
        paths.append(valid)

    return paths[len(paths)-1]

print(task())