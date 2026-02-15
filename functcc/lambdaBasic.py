def filterList(listNos,func):
    result=[]
    for i in listNos:
        if func(i):
            result.append(i)
    return result
print(filterList([1,2,4,5,6,7,89,90],lambda n:n>3))
print(filterList([1,2,4,5,6,7,89,90],lambda n:n>7))
print(filterList([1,2,4,5,6,7,89,90],lambda n:n%2==0))

