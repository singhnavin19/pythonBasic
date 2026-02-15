listNos=[1,2,3,54,6,7,78,9]

def lesstThanNumberFilter(nos,criteria):
    resut=[]
    for i in nos:
        if i<criteria:
            resut.append(i)
    return resut

def GreaterThanNumberFilter(nos,criteria):
    resut=[]
    for i in nos:
        if i>criteria:
            resut.append(i)
    return resut

print(lesstThanNumberFilter(listNos,10))
