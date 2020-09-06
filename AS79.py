def make_it_laugh(x):
    if 'a' in x:
        x = x.replace("a","haha")
    if 'e' in x:
        x = x.replace("e","haha")
    if 'i' in x:
        x = x.replace("i","haha")
    if 'o' in x:
        x = x.replace("o","haha")
    if 'u' in x:
        x = x.replace("u","haha")
    return x
word = str(input("enter your string...: "))
result = make_it_laugh(word)
print(result)