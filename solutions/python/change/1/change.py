
from itertools import combinations_with_replacement
def find_fewest_coins(coins, target):
    

    if target == 0:
        return []

    if target < 0:
        raise ValueError("target can't be negative")
    
    max_coins = target // min(coins)
        
    for i in range(1, max_coins + 1):

        combos = combinations_with_replacement(coins, i)

        for combo in combos:

            if sum(combo) == target:
                return sorted(combo)

    
    raise ValueError("can't make target with given coins")