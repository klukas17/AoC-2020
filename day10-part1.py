def task():
    inputText = open("day10.txt", "r").readlines()
    for line in inputText:
        line.strip("\n")
    numbers = [int(line) for line in inputText]
    numbers.append(0)
    numbers.append(max(numbers)+3)
    numbers.sort()

    dif1 = 0
    dif2 = 0
    dif3 = 0

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] == 1:
            dif1 += 1
        if numbers[i] - numbers[i - 1] == 2:
            dif2 += 1
        if numbers[i] - numbers[i - 1] == 3:
            dif3 += 1
    
    return dif1 * dif3

print(task())