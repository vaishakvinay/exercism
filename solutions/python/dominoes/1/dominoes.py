def can_chain(dominoes):
    
    if not dominoes:
        return []

    
    for i in range(len(dominoes)):
        start = dominoes[i]
        remaining = dominoes[:i] + dominoes[i+1:]

        
        for first in (start, start[::-1]):
            chain = [first]

            if backtrack(chain, remaining):
                return chain

    return None


def backtrack(chain, remaining):
   
    if not remaining:
        return chain[0][0] == chain[-1][1]

    current_end = chain[-1][1]

    
    for i in range(len(remaining)):
        a, b = remaining[i]

        rest = remaining[:i] + remaining[i+1:]

        
        if a == current_end:
            chain.append((a, b))

            if backtrack(chain, rest):
                return True

            chain.pop() 

        
        if b == current_end:
            chain.append((b, a))

            if backtrack(chain, rest):
                return True

            chain.pop()  

    return False



