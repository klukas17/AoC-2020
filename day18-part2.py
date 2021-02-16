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
        
        result += calculate(elements)

    return result

def calculate(elements):
    
    operatorStack = []
    operandStack = []

    for el in elements:

        if el not in ["(", ")", "+", "*"]:
            operandStack.append(el)

        elif el == "(":
            operatorStack.append(el)

        elif el == ")":
            while operatorStack[len(operatorStack)-1] != "(":
                operator = operatorStack.pop()
                operand1 = operandStack.pop()
                operand2 = operandStack.pop()

                if operator == "+":
                    operandStack.append(operand1 + operand2)
                else:
                    operandStack.append(operand1 * operand2)

            operatorStack.pop()

        else:

            while operatorStack != [] and operatorPrecedence(el) <= operatorPrecedence(operatorStack[len(operatorStack)-1]):
                operator = operatorStack.pop()
                operand1 = operandStack.pop()
                operand2 = operandStack.pop()

                if operator == "+":
                    operandStack.append(operand1 + operand2)
                else:
                    operandStack.append(operand1 * operand2)

            operatorStack.append(el)

    while len(operatorStack) != 0:
        operator = operatorStack.pop()
        operand1 = operandStack.pop()
        operand2 = operandStack.pop()

        if operator == "+":
            operandStack.append(operand1 + operand2)
        else:
            operandStack.append(operand1 * operand2)

    return operandStack[0]

def operatorPrecedence(operator):
    if operator == "+":
        return 2
    elif operator == "*":
        return 1
    return 0

print(task())