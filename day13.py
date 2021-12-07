filename = "inputs/input13.txt"


def earliest_departure(lines):
    earliest_time = int(lines[0])
    bus_time = earliest_time
    bus_timestamps = lines[1].split(",")
    bus_timestamps = [int(bus) for bus in bus_timestamps if bus != "x"]
    while True:
        for bus in bus_timestamps:
            if not bus_time % bus:
                return bus * (bus_time - earliest_time)
        bus_time += 1


def check_condition(bus, earliest_timestamp):
    for i in range(1, len(bus)):
        if bus[i] == "x":
            pass
        elif (earliest_timestamp + i) % int(bus[i]):
            return False
    return True


def find_cycle(current_cycle, current_offset, y, offset):
    i = current_offset
    while True:
        if (i + offset) % y == 0:
            return current_cycle * y, i
        i += current_cycle


def timestamp_contest(lines):
    bus_timestamps = lines[1].split(",")
    ys = [int(bus) for bus in bus_timestamps if bus != "x"]
    offset = [i for i, bus in enumerate(bus_timestamps) if bus != "x"]
    current_cycle = ys[0]
    current_offset = 0
    for y, o in zip(ys[1:], offset[1:]):
        current_cycle, current_offset = find_cycle(current_cycle, current_offset, y, o)
    return current_offset


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part", earliest_departure(input))

    print("Second part", timestamp_contest(input))
