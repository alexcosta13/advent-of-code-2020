FILENAME = "inputs/input16.txt"


def column(matrix, i):
    return [row[i] for row in matrix]


def parse_rule(rule):
    value = [
        int(num)
        for elem in rule.split(": ")[1].split(" or ")
        for num in elem.split("-")
    ]
    return {rule.split(": ")[0]: value}


def parse_rules(rules):
    parsed_rules = {}
    for rule in rules:
        parsed_rules.update(parse_rule(rule))
    return parsed_rules


def parse_ticket(ticket):
    return list(map(int, ticket.split(",")))


def parse_tickets(tickets):
    parsed_tickets = []
    for ticket in tickets:
        parsed_tickets.append(parse_ticket(ticket))
    return parsed_tickets


def parse_input(lines):
    rules, own_ticket, tickets = lines.split("\n\n")
    return {
        "rules": parse_rules(rules.split("\n")),
        "own_ticket": parse_ticket(own_ticket.split("\n")[1]),
        "tickets": parse_tickets(tickets.split("\n")[1:])
        + [parse_ticket(own_ticket.split("\n")[1])],
    }


def check_rule(num, rules):
    for rule in rules:
        if rule[0] <= num <= rule[1] or rule[2] <= num <= rule[3]:
            return True
    return False


def filter_tickets(tickets, rules):
    return [ticket for ticket in tickets if is_field_correct(ticket, rules)]


def get_incorrect_field(ticket, rules):
    for num in ticket:
        if not check_rule(num, rules):
            return num
    return 0


def is_field_correct(ticket, rules):
    for num in ticket:
        if not check_rule(num, rules):
            return False
    return True


def valid_rule(nums, rule):
    return all([check_rule(num, [rule]) for num in nums])


def valid_rules(nums, rules):
    valid = []
    for key, rule in rules.items():
        if valid_rule(nums, rule):
            valid.append(key)
    return valid


def basic(data):
    error = 0
    for ticket in data["tickets"]:
        error += get_incorrect_field(ticket, data["rules"].values())
    return error


def advanced(data):
    tickets = filter_tickets(data["tickets"], data["rules"].values())
    number_of_fields = len(data["rules"].keys())
    candidate_fields = [[] for _ in range(number_of_fields)]
    for i, field in enumerate(candidate_fields):
        field += valid_rules(column(tickets, i), data["rules"])

    assigned_fields = []
    while len(assigned_fields) < number_of_fields:
        for i, field in enumerate(candidate_fields):
            if len(field) == 1 and field[0] not in assigned_fields:
                assigned_fields.append(field[0])
            if len(field) > 1:
                candidate_fields[i] = [c for c in field if c not in assigned_fields]

    fields = [f[0] for f in candidate_fields]
    total = 1
    for i, field in enumerate(fields):
        if "departure" in field:
            total *= data["own_ticket"][i]

    return total


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.read()

    data = parse_input(lines)

    part1 = basic(data)
    print("First part:", part1)

    part2 = advanced(data)
    print("Second part:", part2)
