filename = "input13.txt"


def earliestDeparture(lines):
    earliestTime = int(lines[0])
    busTime = earliestTime
    busTimestamps = lines[1].split(",")
    busTimestamps = [int(bus) for bus in busTimestamps if bus != "x"]
    while True:
        for bus in busTimestamps:
            if not busTime % bus:
                return bus * (busTime - earliestTime)
        busTime += 1


def checkCondition(bus, earliestTimestamp):
    for i in range(1, len(bus)):
        if bus[i] == "x":
            pass
        elif (earliestTimestamp + i) % int(bus[i]):
            return False
    return True


def findCycle(currentCycle, currentOffset, y, offset):
    i = currentOffset
    while True:
        if (i + offset) % y == 0:
            return currentCycle * y, i
        i += currentCycle


def timestampContest(lines):
    busTimestamps = lines[1].split(",")
    ys = [int(bus) for bus in busTimestamps if bus != "x"]
    offset = [i for i, bus in enumerate(busTimestamps) if bus != "x"]
    currentCycle = ys[0]
    currentOffset = 0
    for y, o in zip(ys[1:], offset[1:]):
        currentCycle, currentOffset = findCycle(currentCycle, currentOffset, y, o)
    return currentOffset


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part", earliestDeparture(input))

    print("Second part", timestampContest(input))
