filename="input3.txt"

def countTrees(lines, columnStep = 3, rowStep = 1):
    totalTrees = 0
    numRows = len(lines)
    numCols = len(lines[0])
    for i in range(0,int((numRows)/rowStep)):
        square = lines[i * rowStep][(i * columnStep) % numCols]
        if(square == '#'):
            totalTrees += 1
    return totalTrees

with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print('First part:', countTrees(input))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1
for slope in slopes:
    total *= countTrees(input, slope[0], slope[1])

print('Second part:', total)
