filename = "inputs/input06.txt"


def count_answered_questions(line, questions="abcdefghijklmnopqrstuvwxyz"):
    answered_questions = 0
    for q in questions:
        if q in line:
            answered_questions += 1
    return answered_questions


def count_answered_by_everyone(l, questions="abcdefghijklmnopqrstuvwxyz"):
    answered_questions = 0
    for q in questions:
        flag = True
        for item in l:
            if q not in item:
                flag = False
        if flag:
            answered_questions += 1
    return answered_questions


def total_answered_questions_by_everyone(lines):
    total = 0
    current_group = []
    for line in lines:
        if line == "":
            total += count_answered_by_everyone(current_group)
            current_group = []
        else:
            current_group.append(line)
    total += count_answered_by_everyone(current_group)
    return total


def total_answered_questions(lines):
    total = 0
    current_group = ""
    for line in lines:
        if line == "":
            total += count_answered_questions(current_group)
            current_group = ""
        else:
            current_group += line
    total += count_answered_questions(current_group)
    return total


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", total_answered_questions(input))

print("Second part:", total_answered_questions_by_everyone(input))
