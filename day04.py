filename = "inputs/input04.txt"


def valid_passport(passport):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    keys = passport.keys()
    intersection = [value for value in fields if value in keys]
    return len(intersection) == len(fields)


def is_hex_color(value):
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


def advanced_valid_passport(passport):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
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
        if int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76:
            return False
    elif passport["hgt"][-2:] == "cm":
        if int(passport["hgt"][0:-2]) < 150 or int(passport["hgt"][0:-2]) > 193:
            return False
    if not (is_hex_color(passport["hcl"])):
        return False
    if not (passport["ecl"] in eye_color):
        return False
    if (len(passport["pid"]) != 9) or not (passport["pid"].isdigit()):
        return False

    return True


def count_valid_passports(lines, advanced=False):
    valid_passport_function = advanced_valid_passport if advanced else valid_passport
    valid_passports = 0
    current_passport = {}
    for line in lines:
        if line == "":
            if valid_passport_function(current_passport):
                valid_passports += 1
            current_passport = {}
        else:
            for item in line.split(" "):
                current_passport[item.split(":")[0]] = item.split(":")[1]

    # deal with the last passport in case there is no empty line at the end of the file
    if valid_passport_function(current_passport):
        valid_passports += 1
    return valid_passports


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", count_valid_passports(input))

print("First part:", count_valid_passports(input, advanced=True))
