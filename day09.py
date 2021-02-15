filename = "input9.txt"

def addMinMax(l):
    return min(l) + max(l)

def findRange(lines, total):
    acc = 0
    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            acc += lines[j]
            if(acc > total):
                acc = 0
                break
            elif(acc == total):
                return lines[i:j+1]

def findSum(l, total=2020):
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if(l[i] + l[j] == total):
                return True
    return False

def findWeakness(lines, preambleSize = 25):
    for i in range(preambleSize, len(lines)):
        if not findSum(lines[i - preambleSize:i], lines[i]):
            return lines[i]

def findWeaknessAdvanced(lines, preambleSize = 25):
    weakness = findWeakness(lines, preambleSize)
    sumRange = findRange(lines, weakness)
    return addMinMax(sumRange)

with open(filename) as f:
    input = f.readlines()
input = [int(x.strip()) for x in input]

print("First part:", findWeakness(input))

print("Second part:", findWeaknessAdvanced(input))
