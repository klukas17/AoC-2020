def task():
    lines = []
    with open("day21.txt") as f:
        lines = [l.strip() for l in f.readlines()]

    foods = []
    allergenSet = set()
    for line in lines:
        arr = line.split(" (")
        ingredients = arr[0]
        allergens = arr[1]
        allergens = allergens[:len(allergens)-1]
        allergens = allergens.split(", ")
        allergens[0] = allergens[0].split(" ")[1]
        ingredients = ingredients.split(" ")

        allergenSet = allergenSet.union(set(allergens))

        foods.append((set(ingredients), set(allergens)))

        pass

    uncleared = list(allergenSet)

    allergenPairings = []
    
    for allergen in uncleared:
        row = []
        for i in range(len(foods)):
            if allergen in foods[i][1]:
                row.append(i)
        allergenPairings.append([allergen, None, row])

    while True:
        
        num = 0
        for allergen in allergenPairings:
            if allergen[1]:
                num += 1

        if num == len(allergenPairings):
            break

        for i in range(len(allergenPairings)):

            innerFlag = False

            if allergenPairings[i][1]:
                continue

            firstFood = allergenPairings[i][2][0]

            allergenIntersection = foods[firstFood][1]
            foodIntersection = foods[firstFood][0]

            for el in allergenPairings[i][2]:
                allergenIntersection = allergenIntersection.intersection(foods[el][1])
                foodIntersection = foodIntersection.intersection(foods[el][0])

            if len(foodIntersection) == 1 and len(allergenIntersection) == 1:
                foundAllergen = list(foodIntersection)[0]
                allergenPairings[i][1] = foundAllergen

                for food in foods:
                    if foundAllergen in food[0]:
                        food[0].remove(foundAllergen)
                
                innerFlag = True

            if innerFlag:
                break

    print("tu sam")

    allergenList = [allergen[0] for allergen in allergenPairings]
    allergenList.sort()

    dangerous = ""

    for allergen in allergenList:
        for al in allergenPairings:
            if al[0] == allergen:
                dangerous += al[1] + ","
                break

    dangerous = dangerous[:len(dangerous) - 1]

    return dangerous

print(task())