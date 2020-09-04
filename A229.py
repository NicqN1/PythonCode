import random
ipv6hex = ("a","b","c","d","e","f")
ipv6num = (1,2,3,4,5,6,7,8,9)
ipv41 = []
ipv61 =[]
ipv62 =[]
ipv63 = []
ipv64 = []
for x in range(199):
    ipv41.append(x+1)
for i in range(2):
    ipv61.append(random.choice(ipv6hex))
    ipv61.append(random.choice(ipv6num))
    ipv62.append(random.choice(ipv6hex))
    ipv62.append(random.choice(ipv6num))
    ipv63.append(random.choice(ipv6hex))
    ipv63.append(random.choice(ipv6num))
    ipv64.append(random.choice(ipv6hex))
    ipv64.append(random.choice(ipv6num))

print("ipv4 generated:",random.choice(ipv41),":",random.choice(ipv41),":",random.choice(ipv41),":",random.choice(ipv41))
print("ipv6 generated:",ipv61,":",ipv62,":",ipv63,":",ipv64)