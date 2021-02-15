filename="input10.txt"

def countDifferences(lines):
    lines.append(0)
    sortedLines = sorted(lines)
    ones = 0
    threes = 1
    for i in range(1,len(sortedLines)):
        if sortedLines[i] == sortedLines[i - 1] + 1:
            ones += 1
        if sortedLines[i] == sortedLines[i - 1] + 3:
            threes += 1
    return ones*threes

def findNext(lines, current = 0, acc = {}):
    total = 0
    if not lines:
        return 1
    if current in acc.keys():
        return acc[current]
    for i in range(3):
        if(current + i + 1 in lines):
            index = lines.index(current + i + 1)
            nextLines = lines[index + 1:]
            total += findNext(nextLines, lines[index], acc)
    acc[current] = total
    return total

def countDifferentArrangements(lines):
    sortedLines = sorted(lines)
    return findNext(lines=sortedLines)

with open(filename) as f:
    input = f.readlines()
input = [int(x.strip()) for x in input]

print('First part:', countDifferences(input))

print('Second part:', countDifferentArrangements(input))
