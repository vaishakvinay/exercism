
from itertools import combinations

def maximum_value(maximum_weight, items):
    

    best_value = 0

    n = len(items)

    for i in range(n + 1):

        combos = combinations(items, i)

        for combo in combos:

            total_weight = sum(item["weight"] for item in combo)
            total_value  = sum(item["value"]  for item in combo)

            if total_weight <= maximum_weight:
                best_value = max(best_value, total_value)

    return best_value
