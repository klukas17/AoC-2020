def task():
    textInput = open("day09.txt", "r").readlines()
    for line in textInput:
        line.strip("\n")
    numbers = [int(line) for line in textInput]

    queue = []
    for i in range(25):
        queue.append(numbers[i])

    for position in range(25, len(numbers)):
        result = findSum(queue, numbers[position])
        if not result:
            return numbers[position]
        
        queue.append(numbers[position])
        queue.pop(0)

def findSum(queue, number):
    for i in range(25):
        for j in range(i, 25):
            if queue[i] + queue[j] == number:
                return True

    return False

print(task())    