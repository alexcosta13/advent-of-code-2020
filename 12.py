filename = "input12.txt"


def rotate(directionX, directionY, instruction, value):
    x = directionX
    y = directionY
    if instruction == "L":
        for _ in range(int(value / 90)):
            x, y = -y, x
    elif instruction == "R":
        for _ in range(int(value / 90)):
            x, y = y, -x
    return x, y


def manhattanDistance(lines):
    positionX = 0
    positionY = 0
    directionX = 1
    directionY = 0
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


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part:", manhattanDistance(input))
