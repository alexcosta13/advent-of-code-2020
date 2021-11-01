import numpy as np

filename = "input5.txt"


def seatID(line):
    row, column = findSeat(line)
    return row * 8 + column


def findSeat(line, rows=127, columns=8):
    rowInput = line[:7]
    rowCoef = np.array([1 if r == "B" else 0 for r in rowInput])
    rowConst = np.transpose(
        np.array([2 ** i for i in range(6, -1, -1)])
    )  # [64,32,16,8,4,2,1]
    columnInput = line[7:]
    columnCoef = np.array([1 if c == "R" else 0 for c in columnInput])
    columnConst = np.transpose(np.array([2 ** i for i in range(2, -1, -1)]))  # [4,2,1]
    row = rowCoef.dot(rowConst)
    column = columnCoef.dot(columnConst)
    return row, column


# input = 'FBFBBFFRLR'

with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

allIDs = list(map(seatID, input))
max = max(allIDs)
print("The max seat ID is:", max)

sortedIDs = sorted(allIDs)

for i in range(1, len(allIDs)):
    if sortedIDs[i] != sortedIDs[i - 1] + 1:
        print("Your seat ID is:", sortedIDs[i - 1] + 1)
