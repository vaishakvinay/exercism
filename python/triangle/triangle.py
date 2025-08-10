def equilateral(sides):
    if any(side <= 0 for side in sides):
        return False
    return sides[0] == sides[1] == sides[2]
        


def isosceles(sides):
    a, b, c = sides
    if any(side <= 0 for side in sides):
        return False
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return a == b or b == c or c == a
    
def scalene(sides):
    a, b, c = sides
    if any(side <= 0 for side in sides):
        return False
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return a != b and b != c and c != a
