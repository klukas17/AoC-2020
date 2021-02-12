def task():
    textInput = open("day09.txt", "r").readlines()
    for line in textInput:
        line.strip("\n")
    numbers = [int(line) for line in textInput]

    queue = []
    for i in range(25):
        queue.append(numbers[i])

    number = None

    for position in range(25, len(numbers)):
        result = findSum(queue, numbers[position])
        if not result:
            number = numbers[position]
            break
        
        queue.append(numbers[position])
        queue.pop(0)

    sum = 0
    arr = []
    for i in range(len(numbers)):
        sum += numbers[i]
        arr.append(numbers[i])
        for j in range(i+1,len(numbers)):
            sum += numbers[j]
            arr.append(numbers[j])
            if sum > number:
                break
            if sum == number:
                return min(arr) + max(arr)
        sum = 0
        arr = []

def findSum(queue, number):
    for i in range(25):
        for j in range(i, 25):
            if queue[i] + queue[j] == number:
                return True

    return False

print(task())    