from itertools import permutations

def solve():
    houses = range(5)

    for (englishman, spaniard, ukrainian, norwegian, japanese) in permutations(houses):

        if norwegian != 0:
            continue

        for (red, green, ivory, yellow, blue) in permutations(houses):

            if englishman != red:
                continue

            if green != ivory + 1:
                continue

            if abs(norwegian - blue) != 1:
                continue

            for (dog, snails, fox, horse, zebra) in permutations(houses):

                if spaniard != dog:
                    continue

                for (coffee, tea, milk, orange_juice, water) in permutations(houses):

                    if milk != 2:
                        continue

                    if coffee != green:
                        continue

                    if ukrainian != tea:
                        continue

                    for (painter, dancer, reader, football, chess) in permutations(houses):

                        if snails != dancer:
                            continue

                        if yellow != painter:
                            continue

                        if abs(reader - fox) != 1:
                            continue

                        if abs(painter - horse) != 1:
                            continue

                        if football != orange_juice:
                            continue

                        if japanese != chess:
                            continue

                        return {
                            "water": water,
                            "zebra": zebra,
                            "englishman": englishman,
                            "spaniard": spaniard,
                            "ukrainian": ukrainian,
                            "norwegian": norwegian,
                            "japanese": japanese,
                        }


def drinks_water():
    result = solve()
    for nationality in ["englishman", "spaniard", "ukrainian", "norwegian", "japanese"]:
        if result[nationality] == result["water"]:
            return nationality.capitalize()


def owns_zebra():
    result = solve()
    for nationality in ["englishman", "spaniard", "ukrainian", "norwegian", "japanese"]:
        if result[nationality] == result["zebra"]:
            return nationality.capitalize()
