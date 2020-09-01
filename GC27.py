import random
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for x in range(1,21):
    if x%3== 0 and x%5 == 0:
        print("Fizzbu")
    elif x%3 == 0:
        print("fizz")
    elif x%5 == 0:
        print("buzz")
    else:
        print(x)