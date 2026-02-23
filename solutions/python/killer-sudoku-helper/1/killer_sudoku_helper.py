from itertools import combinations as combo

def combinations(target, size, exclude):
    digits = [d for d in range(1, 10) if d not in exclude]
    
    result = []
    
    for c in combo(digits, size):
        if sum(c) == target:
            result.append(list(c))
    
    return result
