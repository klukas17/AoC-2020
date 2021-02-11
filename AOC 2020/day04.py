def part1():

    lines = open("day04.txt", "r").readlines()
    lines.append("\n")
    validPassports = 0
    
    byr = iyr = eyr = hgt = hcl = ecl = pid = False

    for line in lines:

        if line == "\n":
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                validPassports += 1
            byr = iyr = eyr = hgt = hcl = ecl = pid = False
            continue

        arr = line.split(" ")
        fields = [field[:3] for field in arr]

        if "byr" in fields:
            byr = True

        if "iyr" in fields:
            iyr = True

        if "eyr" in fields:
            eyr = True
            
        if "hgt" in fields:
            hgt = True

        if "hcl" in fields:
            hcl = True

        if "ecl" in fields:
            ecl = True

        if "pid" in fields:
            pid = True

    return validPassports

def part2():

    lines = open("day04.txt", "r").readlines()
    lines.append("\n")
    validPassports = 0
    
    byr = iyr = eyr = hgt = hcl = ecl = pid = False

    for line in lines:

        if line == "\n":
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                validPassports += 1
            byr = iyr = eyr = hgt = hcl = ecl = pid = False
            continue

        arr = line.split(" ")
        fields = [field[:3] for field in arr]

        if "byr" in fields:
            for el in arr:
                if el[:3] == "byr":
                    el = el[4:].strip()
                    if len(el) == 4:
                        try:
                            el = int(el)
                            if el >= 1920 and el <= 2002:
                                byr = True
                        except:
                            pass

        if "iyr" in fields:
            for el in arr:
                if el[:3] == "iyr":
                    el = el[4:].strip()
                    if len(el) == 4:
                        try:
                            el = int(el)
                            if el >= 2010 and el <= 2020:
                                iyr = True
                        except:
                            pass

        if "eyr" in fields:
            for el in arr:
                if el[:3] == "eyr":
                    el = el[4:].strip()
                    if len(el) == 4:
                        try:
                            el = int(el)
                            if el >= 2020 and el <= 2030:
                                eyr = True
                        except:
                            pass
            
        if "hgt" in fields:
            for el in arr:
                if el[:3] == "hgt":
                    el = el[4:].strip()
                    unit = el[len(el)-2:len(el)]
                    if unit == "cm":
                        measure = el[:len(el)-2]
                        try:
                            measure = int(measure)
                            if measure >= 150 and measure <= 193:
                                hgt = True
                        except:
                            pass
                    elif unit == "in":
                        measure = el[:len(el)-2]
                        try:
                            measure = int(measure)
                            if measure >= 59 and measure <= 76:
                                hgt = True
                        except:
                            pass

        if "hcl" in fields:
            for el in arr:
                if el[:3] == "hcl":
                    el = el[4:].strip()
                    if el[0] == "#":
                        el = el[1:]
                        literals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
                        flag = True
                        for literal in el:
                            if literal not in literals:
                                flag = False
                        if flag:
                            hcl = True

        if "ecl" in fields:
            for el in arr:
                if el[:3] == "ecl":
                    el = el[4:].strip()
                    eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if el in eyeColors:
                        ecl = True

        if "pid" in fields:
            for el in arr:
                if el[:3] == "pid":
                    el = el[4:].strip()
                    if len(el) == 9:
                        try:
                            el = int(el)
                            pid = True
                        except:
                            pass

    return validPassports

print(part1())
print(part2())