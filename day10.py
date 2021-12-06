filename = "inputs/input10.txt"


def count_differences(lines):
    lines.append(0)
    sorted_lines = sorted(lines)
    ones = 0
    threes = 1
    for i in range(1, len(sorted_lines)):
        if sorted_lines[i] == sorted_lines[i - 1] + 1:
            ones += 1
        if sorted_lines[i] == sorted_lines[i - 1] + 3:
            threes += 1
    return ones * threes


def find_next(lines, current=0, acc=None):
    if acc is None:
        acc = {}
    total = 0
    if not lines:
        return 1
    if current in acc.keys():
        return acc[current]
    for i in range(3):
        if current + i + 1 in lines:
            index = lines.index(current + i + 1)
            next_lines = lines[index + 1 :]
            total += find_next(next_lines, lines[index], acc)
    acc[current] = total
    return total


def count_different_arrangements(lines):
    sorted_lines = sorted(lines)
    return find_next(lines=sorted_lines)


with open(filename) as f:
    input = f.readlines()
input = [int(x.strip()) for x in input]

print("First part:", count_differences(input))

print("Second part:", count_different_arrangements(input))
