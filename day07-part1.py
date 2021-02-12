class Bag():

    def __init__(self, color, subBags):
        self.color = color
        self.subBags = subBags

    def __str__(self):
        subbags = ""
        for bag in self.subBags:
            subbags += bag.color + ", "
        subbags = subbags[:len(subbags)-2]
        return self.color + ": " + subbags

    def getColor(self):
        return self.color

    def getSubBags(self):
        return self.subBags

    def updateSubBags(self, newBags):
        for bag in newBags:
            if bag not in self.subBags:
                self.subBags.append(bag)

    def contains(self, subBag):

        if subBag in self.subBags:
            return True
        
        for bag in self.subBags:
            if bag.contains(subBag):
                return True

        return False

def task():

    inputText = open("day07.txt", "r").readlines()
    allBags = []

    for line in inputText:

        line = line.split(" bags contain ")
        color = line[0]
        line = line[1]
        line = line.split(", ")
        subBagColors = []
        subBags = []

        for el in line:
            el = el.split(" ")
            bagColor = el[1] + " " + el[2]
            subBagColors.append(bagColor)

        for subBagColor in subBagColors:
            subBag = None
            for bag in allBags:
                if bag.color == subBagColor:
                    subBag = bag
                    break
            if not subBag:
                subBagSubBags = []
                subBag = Bag(subBagColor, subBagSubBags)
                allBags.append(subBag)

            subBags.append(subBag)

        newBag = None
        for bag in allBags:
            if bag.color == color:
                newBag = bag
                break
        if newBag:
            newBag.updateSubBags(subBags)
        else:
            newBag = Bag(color, subBags)
            allBags.append(newBag)

    bagColor = "shiny gold"
    searchedBag = None
    for bag in allBags:
        if bag.color == bagColor:
            searchedBag = bag
            break
    result = 0

    for bag in allBags:
        if bag.contains(searchedBag):
            result += 1

    return result

print(task())