filename = "input19.txt"


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
                return (False,)
            else:
                sentence = m[1]
        return True, sentence


def checkRules(r, m, second=False):
    rules = {line.split(": ")[0]: line.split(": ")[1] for line in r.split("\n")}
    sentences = [s for s in m.split("\n")]
    if second:
        rules["8"] = "42 | 42 8"
        rules["11"] = "42 31 | 42 11 31"
    total = 0
    for s in sentences:
        result = match(s, rules["0"], rules)
        if result[0] and result[1] == "":
            total += 1
    return total


if __name__ == "__main__":
    rules, matches = open(filename).read().split("\n\n")

    print('First part:', checkRules(rules, matches))
