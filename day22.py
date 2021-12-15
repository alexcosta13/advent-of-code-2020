filename = "inputs/input22.txt"


def play(d1, d2):
    while d1 and d2:
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if c1 > c2:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
    return d1 if d1 else d2


def pair(d1, d2):
    return d1.__str__() + " " + d2.__str__()


def play_recursive(d1, d2, advanced=False):
    pairs = {}
    while d1 and d2:
        if pair(d1, d2) in pairs:
            return d1, True

        pairs[pair(d1, d2)] = 1
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if len(d1) >= c1 and len(d2) >= c2 and advanced:
            subgameD1 = d1.copy()[:c1]
            subgameD2 = d2.copy()[:c2]
            winner1 = play_recursive(subgameD1, subgameD2, True)[1]
        else:
            winner1 = c1 > c2
        if winner1:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
    return (d1, True) if d1 else (d2, False)


def calculate_score(d):
    total = 0
    coeff = len(d)
    for c in d:
        total += c * coeff
        coeff -= 1
    return total


if __name__ == "__main__":
    player1, player2 = open(filename).read().split("\n\n")

    deck1 = [int(line) for line in player1.split("\n") if line.isnumeric()]
    deck2 = [int(line) for line in player2.split("\n") if line.isnumeric()]

    print("First part:", calculate_score(play_recursive(deck1, deck2)[0]))

    deck1 = [int(line) for line in player1.split("\n") if line.isnumeric()]
    deck2 = [int(line) for line in player2.split("\n") if line.isnumeric()]

    print("Second part:", calculate_score(play_recursive(deck1, deck2, True)[0]))
