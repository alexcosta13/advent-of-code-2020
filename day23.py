def move(cups):
    max_value = max(cups) + 1
    insert_value = (cups[0] - 1) % max_value
    moving = cups[1:4]
    del cups[1:4]
    while insert_value not in cups:
        insert_value = (insert_value - 1) % max_value
    insert_index = cups.index(insert_value) + 1
    cups[insert_index:insert_index] = moving
    cups.append(cups.pop(0))
    return cups


def move_fast(cups, i, max_value):
    move_value = cups[i]
    end_gap = cups[cups[cups[cups[i]]]]
    movers = [cups[i], cups[cups[i]], cups[cups[cups[i]]]]
    cups[i] = end_gap

    insert_value = ((i - 2) % max_value) + 1
    while insert_value in movers:
        insert_value = ((insert_value - 2) % max_value) + 1

    after_gap = cups[insert_value]
    cups[insert_value] = move_value
    cups[movers[-1]] = after_gap

    return cups, cups[i]


def play(input, rounds=100):
    input = [int(i) for i in input]
    for i in range(rounds):
        input = move(input)

    while input[0] != 1:
        input.append(input.pop(0))
    return "".join(str(i) for i in input[1:])


def advanced(input, max=1000000, rounds=10000000):
    input = [int(i) for i in input]
    cups = {input[i]: input[i + 1] for i in range(len(input) - 1)}
    cups[input[-1]] = len(input) + 1
    cups.update({i: i + 1 for i in range(len(input) + 1, max)})
    cups[max] = input[0]
    i = input[0]
    for _ in range(rounds):
        cups, i = move_fast(cups, i, max)
    return cups[1] * cups[cups[1]]


if __name__ == "__main__":
    input = "942387615"

    print("First part:", play(input))
    print("Second part:", advanced(input))
