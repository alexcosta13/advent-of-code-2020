filename = "input12.txt"


def rotate(waypointX, waypointY, instruction, value):
    x = waypointX
    y = waypointY
    if instruction == "L":
        for _ in range(int(value / 90)):
            x, y = -y, x
    elif instruction == "R":
        for _ in range(int(value / 90)):
            x, y = y, -x
    return x, y


def manhattanDistance(lines):
    waypointX = 10
    waypointY = 1
    positionX = 0
    positionY = 0
    for line in lines:
        instruction, value = line[0], int(line[1:])
        if instruction == "E":
            waypointX += value
        elif instruction == "W":
            waypointX -= value
        elif instruction == "N":
            waypointY += value
        elif instruction == "S":
            waypointY -= value
        elif instruction == "F":
            positionX += waypointX * value
            positionY += waypointY * value
        else:
            waypointX, waypointY = rotate(waypointX, waypointY, instruction, value)
    return abs(positionX) + abs(positionY)


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("Second part:", manhattanDistance(input))
