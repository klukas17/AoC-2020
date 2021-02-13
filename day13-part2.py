def task():
    inputText = open("day13.txt", "r").readlines()
    timestamp = inputText[0]
    buses = inputText[1]
    timestamp = timestamp.strip()
    buses = buses.strip()
    timestamp = int(timestamp)
    IDs = []
    buses = buses.split(",")
    for bus in buses:
        if bus != "x":
            IDs.append(int(bus))
        else:
            IDs.append(None)

    modulos = []
    t = -1
    for el in IDs:
        t += 1
        if el:
            modulos.append((el, el - (t % el) if (t % el) != 0 else 0))

    modulos.sort()
    modulos.reverse()

    answer = modulos[0][1]
    n = modulos[0][0]

    for el in modulos[1:]:
        divisor = el[0]
        remainder = el[1]
        while answer % divisor != remainder:
            answer += n 
        n *= divisor
    
    return answer

print(task())
