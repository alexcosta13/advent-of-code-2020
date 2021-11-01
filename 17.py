filename = "input17.txt"


def countAdjacents(lines, x, y, z):
    adjacents = [
        (i, j, k)
        for i in range(-1, 2)
        for j in range(-1, 2)
        for k in range(-1, 2)
        if (i, j, k) != (0, 0, 0)
    ]
    count = 0
    for a in adjacents:
        try:
            if lines[x + a[0]][y + a[1]][z + a[2]] == "#":
                count += 1
        except:
            pass
    return count


def computeEnergy(lines):
    l = []
    for i in range(len(lines)):
        aux = []
        for j in range(len(lines[0])):
            line = ""
            for k in range(len(lines[0][0])):
                if (
                    lines[i][j][k] == "#"
                    and countAdjacents(lines, i, j, k) == 2
                    or countAdjacents(lines, i, j, k) == 3
                ):
                    line += "#"
                elif lines[i][j][k] == "." and countAdjacents(lines, i, j, k) == 3:
                    line += "#"
                else:
                    line += "."
            aux.append(line)
        l.append(aux)
    return l


def countEnergy(world, active="#"):
    total = 0
    for dim in world:
        for d in dim:
            total += d.count(active)
    return total


def adaptInput(lines, extra=30):
    l = []
    dim = len(lines) + extra
    for i in range(dim):
        if i == dim // 2:
            layer = []
            for line in lines:
                line = "." * (extra // 2) + line + "." * (extra // 2)
                layer.append(line)
            for _ in range(dim // 2 - 1):
                layer.append("." * dim)
                layer.insert(0, "." * dim)
            l.append(layer)
        else:
            l.append(["." * dim] * dim)
    return l


def transformEnergy(lines, cycles=6):
    l = adaptInput(lines)
    for _ in range(cycles):
        l = computeEnergy(l)
    return countEnergy(l)


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    #print("First part:", transformEnergy(input, 6))
