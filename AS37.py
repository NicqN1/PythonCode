def rovar(x):
    if 'b' in x:
        x = x.replace('b','bob')
    if "c" in x:
        x = x.replace("c","coc")
    if "d" in x:
        x = x.replace("d","dod")
    if "f" in x:
        x = x.replace("f","fof")
    if "g" in x:
        x = x.replace("g","gog")
    if "h" in x:
        x = x.replace("h","hoh")
    if "j" in x:
        x = x.replace("j","joj")
    if "k" in x:
        x = x.replace("k","kok")
    if "l" in x:
        x = x.replace("l","lol")
    if "m" in x:
        x = x.replace("m","mom")
    if "n" in x:
        x = x.replace("n","non")
    if "p" in x:
        x = x.replace("p","pop")
    if "q" in x:
        x = x.replace("q","qoq")
    if "r" in x:
        x = x.replace("r","ror")
    if "s" in x:
        x = x.replace("s","sos")
    if "t" in x:
        x = x.replace("t","tot")
    if "v" in x:
        x = x.replace("v","vov")
    if "w" in x:
        x = x.replace("w","wow")
    if "x" in x:
        x = x.replace("x","xox")
    if "y" in x:
        x = x.replace("y","yoy")
    if "z" in x:
        x = x.replace("z","zoz")
    return x
inp = input("enter: ")
results = rovar(inp)
print(results)