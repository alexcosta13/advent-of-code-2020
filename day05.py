import numpy as np

filename = "inputs/input05.txt"


def seat_ID(line):
    row, column = find_seat(line)
    return row * 8 + column


def find_seat(line, rows=127, columns=8):
    row_input = line[:7]
    row_coef = np.array([1 if r == "B" else 0 for r in row_input])
    row_const = np.transpose(
        np.array([2 ** i for i in range(6, -1, -1)])
    )  # [64,32,16,8,4,2,1]
    column_input = line[7:]
    column_coef = np.array([1 if c == "R" else 0 for c in column_input])
    column_const = np.transpose(np.array([2 ** i for i in range(2, -1, -1)]))  # [4,2,1]
    row = row_coef.dot(row_const)
    column = column_coef.dot(column_const)
    return row, column


# input = 'FBFBBFFRLR'

with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

all_IDs = list(map(seat_ID, input))
max = max(all_IDs)
print("First part:", max)

sorted_IDs = sorted(all_IDs)

for i in range(1, len(all_IDs)):
    if sorted_IDs[i] != sorted_IDs[i - 1] + 1:
        print("Second part:", sorted_IDs[i - 1] + 1)
