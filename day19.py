filename = "inputs/input19.txt"


def rule_length(rule, rules):
    if rule in ['"a"', '"b"']:
        return 1
    elif "|" in rule:
        return rule_length(rule.split(" | ")[0], rules)
    else:
        t = 0
        for r in rule.split():
            t += rule_length(rules[r], rules)
        return t


def match(sentence, rule, rules):
    if sentence == "":
        return True, ""
    if rule in ['"a"', '"b"']:
        if sentence[0] == rule[1:-1]:
            return True, sentence[1:]
        else:
            return False,
    elif "|" in rule:
        for r in rule.split(" | "):
            m = match(sentence, r, rules)
            if m[0]:
                return True, m[1]
        return False,
    else:
        for r in rule.split():
            m = match(sentence, rules[r], rules)
            if not m[0]:
                return False,
            else:
                sentence = m[1]
        return True, sentence


def basic(rules, sentences):
    total = 0
    for s in sentences:
        result = match(s, rules["0"], rules)
        if result[0] and result[1] == "":
            total += 1
    return total


def advanced(rules, sentences):
    total = 0
    len42 = rule_length(rules["42"], rules)

    for s in sentences:
        flag31 = False
        if match(s[:len42], rules["42"], rules)[0]:
            s = s[len42:]
            while (
                match(s[:len42], rules["42"], rules)[0]
                and match(s[-len42:], rules["31"], rules)[0]
                and s != ""
            ):
                s = s[len42:-len42]
                flag31 = True
        while match(s[:len42], rules["42"], rules)[0] and s != "":
            s = s[len42:]

        if s == "" and flag31:
            total += 1

    return total


if __name__ == "__main__":
    rules, matches = open(filename).read().split("\n\n")

    rules = {line.split(": ")[0]: line.split(": ")[1] for line in rules.split("\n")}
    sentences = [s for s in matches.split("\n")]

    print("First part:", basic(rules, sentences))
    print("Second part:", advanced(rules, sentences))
