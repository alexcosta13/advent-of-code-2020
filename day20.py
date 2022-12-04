import math
from collections import Counter

FILENAME = "inputs/input20.txt"


class Tile:
    def __int__(self):
        pass

    def __init__(self, *args):
        if len(args) == 1:
            data = args[0]
            self.id = int(data.split("\n")[0].split("Tile ")[1][:-1])
            self.data = [
                [0 if i == "." else 1 for i in d] for d in data.split("\n")[1:]
            ]
        elif len(args) == 0:
            pass

    @staticmethod
    def tile_from_data(data):
        t = Tile()
        t.data = data
        return t

    def rotate(self):
        self.data = [
            [self.data[j][i] for j in range(len(self.data))]
            for i in range(len(self.data[0]) - 1, -1, -1)
        ]

    def rotate2(self):
        self.data = list(zip(*self.data[::-1]))

    def flip(self):
        self.data = [line[::-1] for line in self.data]

    def get_edges(self):
        return [
            self.data[0],
            self.data[-1],
            [x[0] for x in self.data],
            [x[-1] for x in self.data],
        ]

    def get_edges_aux(self):
        return [
            tuple(self.data[0]),
            tuple(self.data[-1]),
            tuple([x[0] for x in self.data]),
            tuple([x[-1] for x in self.data]),
        ]

    def get_edges2(self):
        edges = []
        for _ in range(2):
            edges.extend(self.get_edges_aux())
            self.flip()
        self.rotate()
        for _ in range(2):
            edges.extend(self.get_edges_aux())
            self.flip()
        for _ in range(3):
            self.rotate()
        return edges

    def get_right_edge(self):
        return [x[-1] for x in self.data]

    def get_left_edge(self):
        return [x[0] for x in self.data]

    def get_bottom_edge(self):
        return self.data[-1]

    def get_upper_edge(self):
        return self.data[0]

    def remove_borders(self):
        self.data = [x[1:-1] for x in self.data[1:-1]]

    def is_neighbor(self, other):
        for edge in self.get_edges2():
            if edge in other.get_edges2():
                return True
        return False

    def __hash__(self):
        return self.id


def get_neighbors(tiles):
    count = []
    neighbors = set()
    for tile1 in tiles:
        for tile2 in tiles:
            if tile1 != tile2:
                for _ in range(4):
                    edges1 = tile1.get_edges()
                    tile1.rotate()
                    for _ in range(4):
                        edges2 = tile2.get_edges()
                        tile2.rotate()
                        for edge in edges2:
                            if edge in edges1:
                                count.append(tile1)
                                count.append(tile2)
                                neighbors.add((tile1, tile2))

    count = {k: v / 16 for k, v in Counter(count).items()}
    return neighbors, count


def sort_tiles(pairs, count):
    side_length = int(math.sqrt(len(count)))
    partner = {}
    for a, b in pairs:
        partner[a] = partner.get(a, set()) | {b}
        partner[b] = partner.get(b, set()) | {a}
    for a, b in partner.items():
        partner[a] = list(b)
    corner = [k for k, v in count.items() if v == 2]
    border = [k for k, v in count.items() if v == 3]
    center = [k for k, v in count.items() if v == 4]
    grid = [[None for _ in range(side_length)] for _ in range(side_length)]
    for i in range(side_length):
        for j in range(side_length):
            if i == 0 and j == 0:
                grid[i][j] = corner.pop()
            elif i == 0 and j == side_length - 1:
                new_tile = (
                    partner[grid[i][j - 1]][0]
                    if partner[grid[i][j - 1]][0] in corner
                    else partner[grid[i][j - 1]][1]
                )
                corner.remove(new_tile)
                partner[grid[i][j - 1]].remove(new_tile)
                partner[new_tile].remove(grid[i][j - 1])
                grid[i][j] = new_tile
            elif i == side_length - 1 and j == 0:
                new_tile = (
                    partner[grid[i - 1][j]][0]
                    if partner[grid[i - 1][j]][0] in corner
                    else partner[grid[i - 1][j]][1]
                )
                corner.remove(new_tile)
                partner[grid[i - 1][j]].remove(new_tile)
                partner[new_tile].remove(grid[i - 1][j])
                grid[i][j] = new_tile

            elif i == side_length - 1 and j == side_length - 1:
                assert len(border) == len(center) == 0 and len(corner) == 1
                grid[i][j] = corner.pop()
            elif i == 0 or i == side_length - 1:
                new_tile = (
                    partner[grid[i][j - 1]][0]
                    if partner[grid[i][j - 1]][0] in border
                    else partner[grid[i][j - 1]][1]
                )
                border.remove(new_tile)
                partner[grid[i][j - 1]].remove(new_tile)
                partner[new_tile].remove(grid[i][j - 1])
                grid[i][j] = new_tile
            elif j == 0 or j == side_length - 1:
                new_tile = (
                    partner[grid[i - 1][j]][0]
                    if partner[grid[i - 1][j]][0] in border
                    else partner[grid[i - 1][j]][1]
                )
                border.remove(new_tile)
                partner[grid[i - 1][j]].remove(new_tile)
                partner[new_tile].remove(grid[i - 1][j])
                grid[i][j] = new_tile
            else:
                new_tile = (
                    partner[grid[i - 1][j]][0]
                    if partner[grid[i - 1][j]][0] in center
                    else partner[grid[i - 1][j]][1]
                )
                center.remove(new_tile)
                partner[grid[i - 1][j]].remove(new_tile)
                partner[grid[i][j - 1]].remove(new_tile)
                partner[new_tile].remove(grid[i - 1][j])
                partner[new_tile].remove(grid[i][j - 1])
                grid[i][j] = new_tile
    return grid


def rotate_grid(grid):
    first = grid[0][0]
    first.flip()
    second = grid[0][1]
    opp = grid[1][0]
    for _ in range(2):
        for _ in range(2):
            for _ in range(4):
                for _ in range(4):
                    if first.get_right_edge() == second.get_left_edge():
                        if tuple(first.get_bottom_edge()) in opp.get_edges2():
                            return first_in_place(grid)
                    second.rotate2()
                first.rotate2()
            second.flip()
        first.flip()
    raise NotImplementedError()


def first_in_place(grid):
    for i in range(2, len(grid)):
        tile = grid[0][i]
        k = 0
        while grid[0][i - 1].get_right_edge() != tile.get_left_edge():
            tile.rotate() if k % 4 else tile.flip()
            k += 1
    for i in range(1, len(grid)):
        tile = grid[i][0]
        k = 0
        while tuple(grid[i - 1][0].get_bottom_edge()) != tuple(tile.get_upper_edge()):
            tile.rotate() if k % 4 else tile.flip()
            k += 1
        for j in range(1, len(grid)):
            tile = grid[i][j]
            k = 0
            while grid[i][j - 1].get_right_edge() != tile.get_left_edge():
                tile.rotate() if k % 4 else tile.flip()
                k += 1
    return grid


def mash_grid(grid):
    final_grid = [[] for _ in range(len(grid) * 8)]

    for i in range(len(grid)):
        for j in range(len(grid)):
            tile = grid[i][j]
            tile.remove_borders()

            for k in range(8):
                final_grid[8 * i + k] += tile.data[k]
    return final_grid


def is_monster(grid, monster, position):
    total = sum([sum(line) for line in monster])
    count = 0
    x, y = position
    for i in range(len(monster)):
        for j in range(len(monster[0])):
            try:
                count += monster[i][j] * grid[i + x][j + y]
            except:
                return False
    return total == count


def add_monster(monster_grid, monster, position):
    x, y = position
    for i in range(len(monster)):
        for j in range(len(monster[0])):
            monster_grid[i + x][j + y] = min(
                1, monster_grid[i + x][j + y] + monster[i][j]
            )
    return monster_grid


def water_roughness(original_grid, monster_grid):
    roughness = 0
    for i in range(len(original_grid)):
        for j in range(len(original_grid[0])):
            if original_grid[i][j] == 1 and monster_grid[i][j] == 0:
                roughness += 1
    return roughness


def basic(tiles):
    _, count = get_neighbors(tiles)
    count = [k.id for k, v in count.items() if v == 2]
    return math.prod(count)


def advanced(tiles):
    pairs, count = get_neighbors(tiles)
    grid = sort_tiles(pairs, count)
    correct_grid = rotate_grid(grid)
    final_grid = Tile.tile_from_data(mash_grid(correct_grid))
    monster = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    ]

    monster_grid = [
        [0 for _ in range(len(final_grid.data[0]))] for _ in range(len(final_grid.data))
    ]

    monster_found = False
    k = 0
    while not monster_found:
        final_grid.rotate() if k % 4 else final_grid.flip()
        for i in range(len(final_grid.data)):
            for j in range(len(final_grid.data[0])):
                if is_monster(final_grid.data, monster, (i, j)):
                    monster_grid = add_monster(monster_grid, monster, (i, j))
                    monster_found = True
        k += 1

    return water_roughness(final_grid.data, monster_grid)


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.read()
    lines = [Tile(x.strip()) for x in lines.split("\n\n")]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
