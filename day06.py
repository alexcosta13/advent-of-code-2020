filename = "input6.txt"


def countAnsweredQuestions(line, questions="abcdefghijklmnopqrstuvwxyz"):
    answeredQuestions = 0
    for q in questions:
        if q in line:
            answeredQuestions += 1
    return answeredQuestions


def countAnsweredByEveryone(l, questions="abcdefghijklmnopqrstuvwxyz"):
    answeredQuestions = 0
    for q in questions:
        flag = True
        for item in l:
            if q not in item:
                flag = False
        if flag:
            answeredQuestions += 1
    return answeredQuestions


def totalAnsweredQuestionsByEveryone(lines):
    total = 0
    currentGroup = []
    for line in lines:
        if line == "":
            total += countAnsweredByEveryone(currentGroup)
            currentGroup = []
        else:
            currentGroup.append(line)
    total += countAnsweredByEveryone(currentGroup)
    return total


def totalAnsweredQuestions(lines):
    total = 0
    currentGroup = ""
    for line in lines:
        if line == "":
            total += countAnsweredQuestions(currentGroup)
            currentGroup = ""
        else:
            currentGroup += line
    total += countAnsweredQuestions(currentGroup)
    return total


with open(filename) as f:
    input = f.readlines()
input = [x.strip() for x in input]

print("First part:", totalAnsweredQuestions(input))

print("Second part:", totalAnsweredQuestionsByEveryone(input))
