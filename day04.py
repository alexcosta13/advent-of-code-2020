filename = "input04.txt"


def validPassport(passport):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    keys = passport.keys()
    intersection = [value for value in fields if value in keys]
    print("intersection", intersection)
    print(len(intersection) == len(fields))
    return len(intersection) == len(fields)


def isHexColor(value):
    valid = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    if len(value) != 7:
        return False
    if value[0] != "#":
        return False
    for v in value[1:]:
        if not (v in valid):
            return False
    return True


def advancedValidPassport(passport):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    keys = passport.keys()
    intersection = [value for value in fields if value in keys]
    if len(intersection) != len(fields):
        return False
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False
    if int(passport["iyr"]) < 2010 or int(passport["byr"]) > 2020:
        return False
    if int(passport["eyr"]) < 2020 or int(passport["byr"]) > 2030:
        return False
    if passport["hgt"][-2:] != "cm" and passport["hgt"][-2:] != "in":
        return False
    if passport["hgt"][-2:] == "in":
        if int(passport["hgt"][0:-2]) < 59 or int(passport["hgt"][0:-2]) > 76:
            return False
    elif passport["hgt"][-2:] == "cm":
        if int(passport["hgt"][0:-2]) < 150 or int(passport["hgt"][0:-2]) > 193:
            return False
    if not (isHexColor(passport["hcl"])):
        return False
    if not (passport["ecl"] in eyeColor):
        return False
    if (len(passport["pid"]) != 9) or not (passport["pid"].isdigit()):
        return False

    return True


def countValidPassports(lines):
    validPassports = 0
    currentPassport = {}
    for line in lines:
        if line == "":  # or end of file
            print("currentPassport", currentPassport.keys())
            if advancedValidPassport(currentPassport):
                validPassports += 1
            currentPassport = {}
        else:
            for item in line.split(" "):
                currentPassport[item.split(":")[0]] = item.split(":")[1]
    return validPassports


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", countValidPassports(input))
