filename = "inputs/input07.txt"


def parse_line(line):
    container = line.split(" bags contain ")[0]
    list = line.split(" bags contain ")[1]
    list = list.split(", ")
    if list == ["no other bags."]:
        list = []
    for bag in list:
        b = bag.split(" ")[1] + " " + bag.split(" ")[2]
        list[list.index(bag)] = b
    return [container, list]


def parse_line2(line):
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


def parse_file(lines):
    containers = []
    for line in lines:
        containers.append(parse_line(line))
    return containers


def parse_file2(lines):
    containers = []
    for line in lines:
        containers.append(parse_line2(line))
    return containers


def count_bag(containers, bag):
    bags = 1
    for container in containers:
        if container[0] == bag:
            # if not container[1]:
            #    return 1
            for b in container[1]:
                bags += int(b[0]) * count_bag(containers, b[1])
    return bags


def find_containers(lines, bag="shiny gold"):
    containers = parse_file(lines)
    possible_containers = [bag]

    for container in possible_containers:
        for b in containers:
            if container in b[1]:
                possible_containers.append(b[0])

    return len(list(dict.fromkeys(possible_containers))) - 1


def count_bags(lines, bag="shiny gold"):
    containers = parse_file2(lines)
    return count_bag(containers, bag) - 1


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", find_containers(input))

print("Second part:", count_bags(input))
