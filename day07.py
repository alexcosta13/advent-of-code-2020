filename = "input7.txt"


def parseLine(line):
    container = line.split(" bags contain ")[0]
    list = line.split(" bags contain ")[1]
    list = list.split(", ")
    if list == ["no other bags."]:
        list = []
    for bag in list:
        b = bag.split(" ")[1] + " " + bag.split(" ")[2]
        list[list.index(bag)] = b
    return [container, list]


def parseLine2(line):
    container = line.split(" bags contain ")[0]
    list = line.split(" bags contain ")[1]
    list = list.split(", ")
    if list == ["no other bags."]:
        list = []
    for bag in list:
        num = bag.split(" ")[0]
        b = bag.split(" ")[1] + " " + bag.split(" ")[2]
        list[list.index(bag)] = [num, b]
    return [container, list]


def parseFile(lines):
    containers = []
    for line in lines:
        containers.append(parseLine(line))
    return containers


def parseFile2(lines):
    containers = []
    for line in lines:
        containers.append(parseLine2(line))
    return containers


def countBag(containers, bag):
    bags = 1
    for container in containers:
        if container[0] == bag:
            # if not container[1]:
            #    return 1
            for b in container[1]:
                bags += int(b[0]) * countBag(containers, b[1])
    return bags


def findContainers(lines, bag="shiny gold"):
    containers = parseFile(lines)
    possibleContainers = [bag]

    for container in possibleContainers:
        for b in containers:
            if container in b[1]:
                possibleContainers.append(b[0])

    return len(list(dict.fromkeys(possibleContainers))) - 1


def countBags(lines, bag="shiny gold"):
    totalBags = 0
    containers = parseFile2(lines)
    return countBag(containers, bag) - 1


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", findContainers(input))

print("Second part:", countBags(input))
