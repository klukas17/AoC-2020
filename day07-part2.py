class Bag():

    def __init__(self, color, subBags):
        self.color = color
        self.subBags = subBags

    def __str__(self):
        subbags = ""
        for bag in self.subBags:
            subbags += str(bag[1]) + " " + bag[0].color + ", "
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

    def countSubBags(self):

        if len(self.subBags) == 0:
            return 1

        count = 0

        for bag in self.subBags:
            count += bag[1] * (1 + bag[0].countSubBags())

        return count
        
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
            count = el[0]
            try:
                count = int(count)
            except:
                count = 0
            bagColor = el[1] + " " + el[2]
            subBagColors.append((bagColor, count))

        for subBagColor in subBagColors:
            subBag = None
            for bag in allBags:
                if bag.color == subBagColor[0]:
                    subBag = bag
                    break
            if not subBag:
                subBagSubBags = []
                subBag = Bag(subBagColor[0], subBagSubBags)
                allBags.append(subBag)

            subBags.append((subBag,subBagColor[1]))

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

    return searchedBag.countSubBags()

print(task())