import random
floorlevel = []
floors = int(input("How many floors in the building?"))
for x in range (floors):
    floorlevel.append(x+1)
print("guards vists these floor order:", random.sample(floorlevel, len(floorlevel)))