def task():
    fileInput = open("day18.txt", "r").readlines()
    lines = [line.strip() for line in fileInput]

    result = 0

    for line in lines:
        elements = []
        for c in line:
            if c == " ":
                continue
            elif c in ["(", ")", "+", "*"]:
                elements.append(c) 
            else:
                elements.append(int(c))
        
        elements.insert(0, "(")
        elements.append(")")

        result += calculate(elements)

    return result

def calculate(elements):
    elements = elements[1:len(elements)-1]
    stack = []
    index = 0
    
    while index < len(elements):

        el = elements[index]

        if el not in ["(", ")"]:
            stack.append(el)
            index += 1

        else:
            newStack = [el]
            parentheses = 1
            while parentheses != 0:
                index += 1
                el = elements[index]
                newStack.append(el)
                if el == "(":
                    parentheses += 1
                elif el == ")":
                    parentheses -= 1
            index += 1
                    
            calculatedValue = calculate(newStack)
            stack.append(calculatedValue)

        if len(stack) == 3:
            if stack[1] == "+":
                value = stack[0] + stack[2]
                stack = [value]
            elif stack[1] == "*":
                value = stack[0] * stack[2]
                stack = [value]

    return stack[0]

print(task())