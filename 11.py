filename = "input11.txt"


def count_adjacents(lines, x, y):
    adjacents = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            idi = x + i
            idj = y + j
            if not i and not j:
                pass
            elif idi < 0 or idj < 0 or idi >= len(lines) or idj >= len(lines[0]):
                pass
            elif lines[idi][idj] == "#":
                adjacents += 1
    return adjacents


def change_seats(lines):
    l = []
    for i in range(len(lines)):
        line = ""
        for j in range(len(lines[0])):
            if lines[i][j] == "L" and count_adjacents(lines, i, j) == 0:
                line += "#"
            elif lines[i][j] == "#" and count_adjacents(lines, i, j) >= 4:
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

    print("First part:", occupied_seats(input))
