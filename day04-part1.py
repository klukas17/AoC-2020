def task():

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

print(task())