filename = "input21.txt"


def intersection(list1, list2):
    return [item for item in list1 if item in list2]


def no_allergens(lines, part2=False):
    foods = [x.split(" (contains ")[0].split() for x in lines]
    allergens = [x.split(" (contains ")[1][:-1].split(", ") for x in lines]
    recipe = list(zip(foods, allergens))
    allergens_in_food = {}
    for r in recipe:
        for a in r[1]:
            if a in allergens_in_food:
                allergens_in_food[a] = intersection(allergens_in_food[a], r[0])
            else:
                allergens_in_food[a] = r[0]
    foods_with_allergens = set([i for x in allergens_in_food.values() for i in x])
    non_allergic_foods = [i for x in foods for i in x if i not in foods_with_allergens]
    if not part2:
        return len(non_allergic_foods)
    final = {}
    while allergens_in_food:
        new_allergens_in_food = {}
        for a, f in allergens_in_food.items():
            if len(f) == 1:
                final[a] = f[0]
            else:
                new_allergens_in_food[a] = [i for i in f if i not in final.values()]
        allergens_in_food = new_allergens_in_food
    canonical = ""
    for k, v in sorted(final.items()):
        canonical += v + ","
    return canonical[:-1]


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part:", no_allergens(input))

    print("Second part:", no_allergens(input, True))
