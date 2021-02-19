def task():
    lines = []
    with open("day22.txt") as f:
        lines = [l.strip() for l in f.readlines()]

    player1cards = []
    player2cards = []

    flag = True
    for line in lines:
        if line == "":
            flag = False
            continue
        if line[0] == "P":
            continue

        if flag:
            player1cards.append(int(line))
        else:
            player2cards.append(int(line))

    winner = recursiveCombat(player1cards, player2cards)

    winner = winner[0][::-1]
    value = 0
    for i in range(len(winner)):
        value += (i + 1) * winner[i]

    return value

def recursiveCombat(player1cards, player2cards):

    previousGames = set()

    while True:

        card1 = player1cards.pop(0)
        card2 = player2cards.pop(0)
        
        currentGame = (tuple(player1cards), tuple(player2cards))

        if currentGame in previousGames:
            player1cards.append(card1)
            player1cards.append(card2)
            return (player1cards, 1)
        else:
            previousGames.add(currentGame)
            
        if card1 <= len(player1cards) and card2 <= len(player2cards):
            winner = recursiveCombat(player1cards[:card1].copy(), player2cards[:card2].copy())
            winner = winner[1]
            if winner == 1:
                player1cards.append(card1)
                player1cards.append(card2)
            elif winner == 2:
                player2cards.append(card2)
                player2cards.append(card1)

        else:
        
            if card1 > card2:
                player1cards.append(card1)
                player1cards.append(card2)

            else:
                player2cards.append(card2)
                player2cards.append(card1)

        if len(player1cards) == 0:
            return player2cards, 2

        elif len(player2cards) == 0:
            return player1cards, 1

print(task())