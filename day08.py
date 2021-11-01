filename = "input8.txt"


def acc(lines):
    acc = 0
    i = 0
    l = lines.copy()
    while True:
        line = l[i]
        l[i] = ""
        if not line:
            return acc
        command, value = line.split()
        value = int(value)
        if command == "acc":
            acc += value
            i += 1
        elif command == "jmp":
            i += value
        elif command == "nop":
            i += 1


def accFixed(lines, fix=0):
    acc = 0
    i = 0
    it = 0
    l = lines.copy()
    while i < len(l):
        line = l[i]
        l[i] = ""
        if not line:
            return 0
        command, value = line.split()
        value = int(value)
        if command == "acc":
            acc += value
            i += 1
        elif command == "jmp":
            it += 1
            if it == fix:
                i += 1
            else:
                i += value
        elif command == "nop":
            it += 1
            if it == fix:
                i += value
            else:
                i += 1
    return acc


def fixed(lines):
    fix = 0
    while True:
        acc = accFixed(lines, fix)
        fix += 1
        if acc != 0:
            return acc


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", acc(input))

print("Second part:", fixed(input))
