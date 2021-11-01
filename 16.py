import re

filename = "input16.txt"


def column(matrix, i):
    return [row[i] for row in matrix]


def checkRule(num, rules):
    for rule in rules:
        if num >= rule[0] and num <= rule[1]:
            return True
    return False


def checkTicket(ticket, rules):
    for num in ticket:
        if not checkRule(num, rules):
            return num
    return 0


def parseRules(rules):
    ruleList = []
    for line in rules:
        for rule in re.findall("\d+-\d+", line):
            ruleList.append(list(map(int, rule.split("-"))))
    return ruleList


def parseInput(input):
    iterator = iter(input)
    ruleList = []
    tickets = []
    r = next(iterator)
    while r != "":
        ruleList.append(r)
        r = next(iterator)
    ruleList = parseRules(ruleList)
    next(iterator)
    while next(iterator) != "":
        ownTicket = next(iterator)
    next(iterator)
    for t in iterator:
        tickets.append(list(map(int, t.split(","))))
    return ruleList, ownTicket, tickets


def basicTicketScanning(input):
    rules, _, tickets = parseInput(input)
    error = 0
    for ticket in tickets:
        error += checkTicket(ticket, rules)
    return error


def advancedTicketScanning(input):
    rules, ownTicket, tickets = parseInput(input)
    rules = assignRules(rules)
    return len(tickets)


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part:", basicTicketScanning(input))

    print("Second part:", advancedTicketScanning(input))
