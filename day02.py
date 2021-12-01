filename = "inputs/input02.txt"


def count_passports(lines, second_part=False):
    total = 0
    for line in lines:
        min = int(line.split("-")[0])
        line = line.split("-")[1]
        max = int(line.split(" ")[0])
        ch = line.split(" ")[1][0]
        password = line.split(" ")[2]
        count = password.count(ch)
        if second_part:
            first = password[min - 1] == ch
            second = password[max - 1] == ch
            if not (first and second) and (first or second):
                total += 1
        else:
            if min <= count <= max:
                total += 1
    return total


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", count_passports(input))

print("Second part:", count_passports(input, second_part=True))
