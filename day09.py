filename = "inputs/input09.txt"


def add_min_max(l):
    return min(l) + max(l)


def find_range(lines, total):
    acc = 0
    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            acc += lines[j]
            if acc > total:
                acc = 0
                break
            elif acc == total:
                return lines[i : j + 1]


def find_sum(l, total=2020):
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if l[i] + l[j] == total:
                return True
    return False


def find_weakness(lines, preamble_size=25):
    for i in range(preamble_size, len(lines)):
        if not find_sum(lines[i - preamble_size : i], lines[i]):
            return lines[i]


def find_weakness_advanced(lines, preamble_size=25):
    weakness = find_weakness(lines, preamble_size)
    sum_range = find_range(lines, weakness)
    return add_min_max(sum_range)


with open(filename) as f:
    input = f.readlines()
input = [int(x.strip()) for x in input]

print("First part:", find_weakness(input))

print("Second part:", find_weakness_advanced(input))
