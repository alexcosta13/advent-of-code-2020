filename = "inputs/input12.txt"


def rotate(x, y, instruction, value):
    if instruction == "L":
        for _ in range(int(value / 90)):
            x, y = -y, x
    elif instruction == "R":
        for _ in range(int(value / 90)):
            x, y = y, -x
    return x, y


def basic(lines):
    positionX, positionY = 0, 0
    directionX, directionY = 1, 0
    for line in lines:
        instruction, value = line[0], int(line[1:])
        if instruction == "E":
            positionX += value
        elif instruction == "W":
            positionX -= value
        elif instruction == "N":
            positionY += value
        elif instruction == "S":
            positionY -= value
        elif instruction == "F":
            positionX += directionX * value
            positionY += directionY * value
        else:
            directionX, directionY = rotate(directionX, directionY, instruction, value)
    return abs(positionX) + abs(positionY)


def advanced(lines):
    waypointX, waypointY = 10, 1
    positionX, positionY = 0, 0
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

    print("First part:", basic(input))

    print("Second part:", advanced(input))
