list1 = []
for i in range(0,20):
    list1.append(i)
want = input("What number do you want to find?")
if want in list1:
    print("It is in it")
else:
    print("Sorry but it is not in the list")