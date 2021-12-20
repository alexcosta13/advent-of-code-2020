filename = "inputs/input24.txt"


def line_to_coord(line):
    ew, ns = 0, 0
    line = list(line)
    while line:
        x = line.pop(0)
        if x == "e":
            ew += 2
        elif x == "w":
            ew -= 2
        else:
            x += line.pop(0)
            if x == "ne":
                ns += 1
                ew += 1
            elif x == "sw":
                ns -= 1
                ew -= 1
            elif x == "nw":
                ns += 1
                ew -= 1
            elif x == "se":
                ns -= 1
                ew += 1
    return ew, ns


def count_adjacents(tile, floor):
    black = 0
    neighbors = [(2, 0), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for neighbor in neighbors:
        new_tile = (tile[0] + neighbor[0], tile[1] + neighbor[1])
        if new_tile in floor and floor[new_tile] == 1:
            black += 1
    return black


def art_exhibit(floor):
    neighbors = [(2, 0), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    new_floor = {}
    for tile in floor:
        new_floor[tile] = 0
        for neighbor in neighbors:
            new_tile = (tile[0] + neighbor[0], tile[1] + neighbor[1])
            new_floor[new_tile] = 0
    for tile in new_floor:
        new_floor[tile] = floor[tile] if tile in floor else 0
    for tile in new_floor:
        if count_adjacents(tile, floor) == 2:
            new_floor[tile] = 1
        elif tile in floor and (
            count_adjacents(tile, floor) == 0 or count_adjacents(tile, floor) > 2
        ):
            new_floor[tile] = 0
    new_floor = {k: v for k, v in new_floor.items() if v}
    return new_floor


def turn_tiles(lines, days=0):
    floor = {}
    for line in lines:
        ew, ns = line_to_coord(line)
        if (ew, ns) in floor:
            floor.pop((ew, ns), None)
        else:
            floor[(ew, ns)] = 1
    for _ in range(days):
        floor = art_exhibit(floor)
    return len(floor)


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part:", turn_tiles(input))
    print("Second part:", turn_tiles(input, 100))
