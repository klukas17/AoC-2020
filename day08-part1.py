def task():
    inputText = open("day08.txt", "r").readlines()
    instructions = []
    instructions.append(0)
    for line in inputText:
        arr = line.split(" ")
        arr[1] = arr[1].strip("\n")
        value = 0
        if arr[1][0] == "+":
            value = int(arr[1][1:])
        else:
            value = -1 * int(arr[1][1:])
        instructions.append((arr[0], value))

    return execute(instructions)

def execute(instructions):

    acc = 0
    position = 1
    visited = []

    while True:

        if position in visited:
            return acc

        if instructions[position][0] == "acc":
            acc += instructions[position][1]
            visited.append(position)
            position += 1

        elif instructions[position][0] == "jmp":
            visited.append(position)
            position += instructions[position][1]

        elif instructions[position][0] == "nop":
            visited.append(position)
            position += 1
        
print(task())