def area():
    r = float(input("What is the radius of the circle: "))
    a = (3.142*r)**2
    return a
result = area()
print(round(result,2))

def circum():
    d = float(input("What is the diameter of the circle: "))
    c = (3.142*d)
    return c
result1 = circum()
print(round(result1,2))