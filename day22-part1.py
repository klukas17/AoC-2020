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

    while True:

        card1 = player1cards[0]
        card2 = player2cards[0]

        if card1 > card2:
            card = player1cards.pop(0)
            player1cards.append(card)
            card = player2cards.pop(0)
            player1cards.append(card)

        else:
            card = player2cards.pop(0)
            player2cards.append(card)
            card = player1cards.pop(0)
            player2cards.append(card)

        if len(player1cards) == 0:
            winner = player2cards
            break

        elif len(player2cards) == 0:
            winner = player1cards
            break

    winner = winner[::-1]
    value = 0
    for i in range(len(winner)):
        value += (i + 1) * winner[i]

    return value

print(task())