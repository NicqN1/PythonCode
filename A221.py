def duplicate_remover(x):
    return list(dict.fromkeys(x))

listt = duplicate_remover(["1","4","4","6","5","1"])
print(listt)