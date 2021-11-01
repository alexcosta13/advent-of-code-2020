filename = "input18.txt"


def findP(expression):
    count = 1
    sep = 1
    while count != 0:
        if expression[sep] == "(":
            count += 1
        elif expression[sep] == ")":
            count -= 1
        sep += 1
    return expression[1 : sep - 1], expression[sep:]


def findDigit(expression):
    num = ""
    for s in expression:
        if s.isnumeric():
            num += s
        else:
            break
    return int(num), expression[len(num) :]


def parseInput(expression):
    current = "".join(expression.split())
    parsed = []
    while current:
        ch = current[0]
        if ch == "(":
            expr, current = findP(current)
        elif ch.isnumeric():
            expr, current = findDigit(current)
        else:
            expr, current = ch, current[1:]
        parsed.append(expr)
    return parsed


def evaluate(expression):
    if isinstance(expression, int) or expression in ["+", "*"]:
        return expression
    else:
        return evaluateExpression(expression, True)


def evaluateExpression(expression, advanced=False):
    parsedInput = parseInput(expression)
    total = evaluate(parsedInput[0])
    for i in range(1, len(parsedInput) - 1):
        op = parsedInput[i]
        expr = evaluate(parsedInput[i + 1])
        if op == "+":
            total += expr
        elif op == "*":
            total *= expr
    return total


def evaluateExpressionAdvanced(expression):
    parsedInput = parseInput(expression)
    total = evaluate(parsedInput[0])
    for i in range(1, len(parsedInput) - 1):
        op = parsedInput[i]
        expr = evaluate(parsedInput[i + 1])
        if op == "+":
            total += expr
        elif op == "*":
            total *= expr
    return total


def solve(lines, advanced=False):
    total = 0
    for line in lines:
        value = evaluateExpression(line, advanced)
        total += value
    return total


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part:", solve(input))

    expressions = [
        "1 + (2 * 3) + (4 * (5 + 6))",
        "2 * 3 + (4 * 5)",
        "5 + (8 * 3 + 9 + 3 * 4 * 3)",
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
    ]
    # print(solve(expressions, True))
