filename = "inputs/input17.txt"


def count_adjacents(lines, x, y, z):
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


def count_adjacents_4d(world, x, y, z, w):
    adjacents = [
        (i, j, k, w)
        for i in range(-1, 2)
        for j in range(-1, 2)
        for k in range(-1, 2)
        for w in range(-1, 2)
        if (i, j, k, w) != (0, 0, 0, 0)
    ]
    count = 0
    for a in adjacents:
        try:
            if (x + a[0], y + a[1], z + a[2], w + a[3]) in world:
                count += 1
        except:
            pass
    return count


def compute_energy(lines):
    l = []
    for i in range(len(lines)):
        aux = []
        for j in range(len(lines[0])):
            line = ""
            for k in range(len(lines[0][0])):
                if (
                    lines[i][j][k] == "#"
                    and count_adjacents(lines, i, j, k) == 2
                    or count_adjacents(lines, i, j, k) == 3
                ):
                    line += "#"
                elif lines[i][j][k] == "." and count_adjacents(lines, i, j, k) == 3:
                    line += "#"
                else:
                    line += "."
            aux.append(line)
        l.append(aux)
    return l


def compute_energy_4d(world):
    future_world = {}
    min_values, max_values = min(world.keys()), max(world.keys())
    candidates = [
        (x, y, z, w)
        for x in range(min_values[0] - 12, max_values[0] + 12)
        for y in range(min_values[1] - 12, max_values[1] + 12)
        for z in range(min_values[2] - 12, max_values[2] + 12)
        for w in range(min_values[3] - 12, max_values[3] + 12)
    ]
    for c in candidates:
        if c in world and count_adjacents_4d(world, *c) in (2, 3):
            future_world[c] = 1
        elif c not in world and count_adjacents_4d(world, *c) == 3:
            future_world[c] = 1
    return future_world


def count_energy(world, active="#"):
    total = 0
    for dim in world:
        for d in dim:
            total += d.count(active)
    return total


def adapt_input(lines, extra=30):
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


def list_to_dict(lines):
    dictionary = {}
    for i, line in enumerate(lines):
        for j, elem in enumerate(line):
            if elem == "#":
                dictionary[(i, j, 0, 0)] = 1
    return dictionary


def transform_energy(lines, cycles=6):
    l = adapt_input(lines)
    for _ in range(cycles):
        l = compute_energy(l)
    return count_energy(l)


def advanced(lines, cycles=6):
    world = list_to_dict(lines)
    for _ in range(cycles):
        world = compute_energy_4d(world)
    return len(world)


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part:", transform_energy(input, 6))

    print("Second part:", advanced(input))
