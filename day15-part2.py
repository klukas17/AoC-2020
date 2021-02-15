class Number():
    def __init__(self, number, first):
        self.number = number
        self.last = first
        self.second = first

def task():
    inputText = open("day15.txt", "r").read().strip()
    arr = [int(el) for el in inputText.split(",")]

    turn = 0
    last = None

    hashMap = {}
    
    for el in arr:
        turn += 1
        num = Number(el, turn)
        hashMap[num.number] = num
        last = num

    while turn != 30000000:

        if last.last == last.second:
            next = 0

        else:
            next = last.last - last.second

        num = None
        try:
            num = hashMap[next]
        except:
            pass

        turn += 1

        if num:
            last = num
            last.second = last.last
            last.last = turn

        else:
            last = Number(next, turn)
            hashMap[last.number] = last

    return last.number
    
print(task())