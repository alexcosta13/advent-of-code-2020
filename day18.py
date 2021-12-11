filename = "inputs/input18.txt"


def find_p(expression):
    count = 1
    sep = 1
    while count != 0:
        if expression[sep] == "(":
            count += 1
        elif expression[sep] == ")":
            count -= 1
        sep += 1
    return expression[1 : sep - 1], expression[sep:]


def find_digit(expression):
    num = ""
    for s in expression:
        if s.isnumeric():
            num += s
        else:
            break
    return int(num), expression[len(num) :]


def parse_input(expression):
    current = "".join(expression.split())
    parsed = []
    while current:
        ch = current[0]
        if ch == "(":
            expr, current = find_p(current)
        elif ch.isnumeric():
            expr, current = find_digit(current)
        else:
            expr, current = ch, current[1:]
        parsed.append(expr)
    return parsed


def evaluate(expression, evaluate_function):
    if isinstance(expression, int) or expression in ["+", "*"]:
        return expression
    else:
        return evaluate_function(expression)


def evaluate_expression(expression):
    parsed_input = parse_input(expression)
    total = evaluate(parsed_input[0], evaluate_expression)
    for i in range(1, len(parsed_input) - 1):
        op = parsed_input[i]
        expr = evaluate(parsed_input[i + 1], evaluate_expression)
        if op == "+":
            total += expr
        elif op == "*":
            total *= expr
    return total


def evaluate_expression_advanced(expression):
    parsed_input = parse_input(expression)
    while len(parsed_input) > 1:
        if "+" in parsed_input:
            idx = parsed_input.index("+")
            result = evaluate(
                parsed_input[idx - 1], evaluate_expression_advanced
            ) + evaluate(parsed_input[idx + 1], evaluate_expression_advanced)
            del parsed_input[idx : idx + 2]
            parsed_input[idx - 1] = result
        else:
            idx = parsed_input.index("*")
            result = evaluate(
                parsed_input[idx - 1], evaluate_expression_advanced
            ) * evaluate(parsed_input[idx + 1], evaluate_expression_advanced)
            del parsed_input[idx : idx + 2]
            parsed_input[idx - 1] = result
    return parsed_input[0]


def solve(lines, advanced=False):
    evaluate_function = (
        evaluate_expression_advanced if advanced else evaluate_expression
    )
    total = 0
    for line in lines:
        value = evaluate_function(line)
        total += value
    return total


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part:", solve(input))

    print("Second part:", solve(input, advanced=True))
