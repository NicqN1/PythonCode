import random
rannumb = []
for x in range (1,51):
    rannumb.append(random.randrange(1,51))
mean = sum(rannumb)/len(rannumb)
print("mean:",mean)
print("min:",min(rannumb))
print("max:",max(rannumb))