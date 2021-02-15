class Number():
    def __init__(self, number, first):
        self.number = number
        self.last = first
        self.second = first

def task():
    inputText = open("day15.txt", "r").read().strip()
    arr = [int(el) for el in inputText.split(",")]

    allNumbers = []
    turn = 0
    last = None

    for el in arr:
        turn += 1
        num = Number(el, turn)
        allNumbers.append(num)
        last = num

    while turn != 2020:

        if last.last == last.second:
            next = 0

        else:
            next = last.last - last.second

        num = None
        for el in allNumbers:
            if el.number == next:
                num = el
                break

        turn += 1

        if num:
            last = num
            last.second = last.last
            last.last = turn

        else:
            last = Number(next, turn)
            allNumbers.append(last)

    return last.number
    
print(task())