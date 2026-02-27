def sum_of_multiples(limit, multiples):
    
    result=[]
    for num in range (1,limit):
        for factor in multiples:
            if factor*num<limit:
                result.append(factor*num)
    result=set(result)

    return sum(result)