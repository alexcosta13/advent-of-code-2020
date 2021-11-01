filename = "input11.txt"


def occupied(lines, x, y, direction):
    distance = 1
    while True:
        if x + distance * direction[0] >= len(lines) or y + distance * direction[
            1
        ] >= len(lines[0]):
            return False
        elif x + distance * direction[0] < 0 or y + distance * direction[1] < 0:
            return False
        elif lines[x + distance * direction[0]][y + distance * direction[1]] == "#":
            return True
        elif lines[x + distance * direction[0]][y + distance * direction[1]] == "L":
            return False
        else:
            distance += 1


def count_adjacents(lines, x, y):
    adjacents = 0
    directions = [
        (i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)
    ]
    for direction in directions:
        if occupied(lines, x, y, direction):
            adjacents += 1
    return adjacents


def change_seats(lines):
    l = []
    for i in range(len(lines)):
        line = ""
        for j in range(len(lines[0])):
            if lines[i][j] == "L" and count_adjacents(lines, i, j) == 0:
                line += "#"
            elif lines[i][j] == "#" and count_adjacents(lines, i, j) >= 5:
                line += "L"
            else:
                line += lines[i][j]
        l.append(line)
    return l


def count_seats(lines, occupied="#"):
    total = 0
    for line in lines:
        total += line.count(occupied)
    return total


def occupied_seats(lines):
    l = list(lines)
    while True:
        newList = change_seats(l)
        if newList == l:
            break
        else:
            l = newList
    return count_seats(l)


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("Second part:", occupied_seats(input))
