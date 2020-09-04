import random
import uuid
ipv6hex = ("a","b","c","d","e","f")
ipv6num = (1,2,3,4,5,6,7,8,9)
ipv41 = []
ipv61 =[]
ipv62 =[]
ipv63 = []
ipv64 = []
for x in range(199):
    ipv41.append(x+1)
def my_random_string(string_length=10):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]
for i in range(0,99):
    print("ipv6 generated:",my_random_string(4),":",my_random_string(4),":",my_random_string(4),":",my_random_string(4))
    print("ipv4 generated:",random.choice(ipv41),":",random.choice(ipv41),":",random.choice(ipv41),":",random.choice(ipv41))