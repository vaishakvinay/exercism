def append(list1, list2):
    
    new=list1+list2

    return new


def concat(lists):
    new=[]
    for lst in lists:
        new +=lst
    return new


def filter(function, list):
    result = []

    for item in list:
        if function(item):
            result.append(item)

    return result


def length(list):
    
    count=0
    for i in list:
        count+=1
    return count

def map(function, list):
    

    result = []

    for item in list:
        result.append(function(item))

    return result


def foldl(function, list, initial):
    result = initial

    for item in list:
        result = function(result, item)

    return result

def foldr(function, list, initial):
    result = initial

    for i in range(len(list) - 1, -1, -1):
        result = function(result, list[i])

    return result

def reverse(list):
    new = []

    for i in range(len(list) - 1, -1, -1):
        new.append(list[i])

    return new