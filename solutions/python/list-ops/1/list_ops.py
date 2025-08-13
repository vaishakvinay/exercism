def append(list1, list2):
    result = []
    # copy all from list1
    for item in list1:
        result += [item]   # add single element as a list
    # copy all from list2
    for item in list2:
        result += [item]
    return result


def concat(lists):
    result = []
    for sublist in lists:
        for item in sublist:
            result += [item]   # add element to result
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):  # Keep only items that match the condition
            result.append(item)
    return result

def length(list):
    count=0
    for l in list:
        count+=1
    return count


def map(function, list):
    result = []
    for item in list:
        result += [function(item)]   # add one transformed item
    return result

def foldl(function, list, initial):
    for item in list:           # process from left to right
        initial= function(initial, item)
    return initial

def foldr(function, list, initial):
    for item in reversed(list):           # process from left to right
        initial= function(initial, item)
    return initial


def reverse(list):
    result = []
    for item in list:
        result = [item] + result  # prepend each element
    return result