isbndigits = []
multiplier = [10,9,8,7,6,5,4,3,2]
isbnmulti = []
for x in range(9):
    isbn = int(input("Input the digit of your isbn:"))
    isbndigits.append(isbn)
checkdigit = int(input("Input the last digit of your isbn (checkdigit):"))
for i in range(9):
    isbnmulti.append(isbndigits[i]*multiplier[i])
isbnsum = sum(isbnmulti)
modulo = isbnsum%11
final = 11 - modulo
print(final)