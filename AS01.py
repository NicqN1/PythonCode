Temp = []
MyList = [9,3,4,5,7,8,10,12,13,6]
n = len(MyList)
boundary = n-1
while boundary > 0:
    for j in range(boundary):
        if MyList[j] > MyList[j+1]:
            Temp = MyList[j]
            MyList[j] = MyList[j+1]
            MyList[j+1] = Temp
    boundary = boundary - 1
print(MyList)