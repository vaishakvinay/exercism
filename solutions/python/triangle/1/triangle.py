def equilateral(sides):
    a, b, c = sides


    if (a + b >= c and b + c >= a  and a + c >= b and a != 0 and b!=0 and c!= 0):

        return a == b == c
    return False
    
def isosceles(sides):
    a, b, c = sides
    if (a + b >= c and b + c >= a  and a + c >= b and a != 0 and b!=0 and c!= 0):

        return a == b or b == c or a == c
    return False

def scalene(sides):
    a, b, c = sides

    if (a + b >= c and b + c >= a  and a + c >= b and a != 0 and b!=0 and c!= 0):

        return a != b and b != c and a != c
    return False