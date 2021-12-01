import re

filename = "inputs/input04.txt"


def valid_passport(passport):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    keys = set(passport.keys()) - {"cid"}
    return keys == fields


def advanced_valid_passport(passport):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    eye_color = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    keys = set(passport.keys()) - {"cid"}
    if keys != fields:
        return False
    if (
        len(passport["byr"]) != 4
        or int(passport["byr"]) < 1920
        or int(passport["byr"]) > 2002
    ):
        return False
    if (
        len(passport["iyr"]) != 4
        or int(passport["iyr"]) < 2010
        or int(passport["byr"]) > 2020
    ):
        return False
    if (
        len(passport["eyr"]) != 4
        or int(passport["eyr"]) < 2020
        or int(passport["byr"]) > 2030
    ):
        return False
    if passport["hgt"][-2:] != "cm" and passport["hgt"][-2:] != "in":
        return False
    if passport["hgt"][-2:] == "in" and (
        int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76
    ):
        return False
    if passport["hgt"][-2:] == "cm" and (
        int(passport["hgt"][0:-2]) < 150 or int(passport["hgt"][0:-2]) > 193
    ):
        return False
    if re.search("^#[a-f0-9]{6}$", passport["hcl"]) is None:
        return False
    if not (passport["ecl"] in eye_color):
        return False
    if re.search("^[0-9]{9}$", passport["pid"]) is None:
        return False

    return True


def count_valid_passports(passports, advanced=False):
    valid_passport_function = advanced_valid_passport if advanced else valid_passport
    valid_passports = 0
    current_passport = {}
    for passport in passports:
        for line in passport.split("\n"):
            for item in line.split(" "):
                current_passport[item.split(":")[0]] = item.split(":")[1]

        if valid_passport_function(current_passport):
            valid_passports += 1
        current_passport = {}

    return valid_passports


with open(filename) as f:
    input = f.read()

passports = input.split("\n\n")
print(len(passports))

print("First part:", count_valid_passports(passports))

print("Second part:", count_valid_passports(passports, advanced=True))
