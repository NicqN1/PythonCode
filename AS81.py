ulist = []
def summ(x):
    a = sum(x)
    return a
for x in range(5):
    alist = int(input("Enter numbers: "))
    ulist.append(alist)

def productt(y):
    resultt = 1
    for i in y:
        resultt = resultt*i
    return resultt
result = summ(ulist)
result1 = productt(ulist)
print("sum: ",result)
print("product: ",result1)