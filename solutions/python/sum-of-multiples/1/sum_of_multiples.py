def sum_of_multiples(limit, multiples):
    
    result=set()
    for i in range(1,limit):
        for m in multiples:
            if m != 0 and i%m==0:
                result.add(i)
    return sum(result)
