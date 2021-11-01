filename = "input03.txt"


def count_trees(lines, column_step=3, row_step=1):
    total_trees = 0
    num_rows = len(lines)
    num_cols = len(lines[0])
    for i in range(0, int(num_rows / row_step)):
        square = lines[i * row_step][(i * column_step) % num_cols]
        if square == "#":
            total_trees += 1
    return total_trees


def count_trees_multiple_slopes(lines, slopes):
    total = 1
    for slope in slopes:
        total *= count_trees(lines, slope[0], slope[1])
    return total


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", count_trees(input))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print("Second part:", count_trees_multiple_slopes(input, slopes))
