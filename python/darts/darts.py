def score(x, y):
    distance = (x**2 + y**2) ** 0.5 
    if distance <= 1.0:
        return 10
    elif distance <= 5.0:
        return 5
    elif distance <= 10.0:
        return 1
    else:
        return 0
