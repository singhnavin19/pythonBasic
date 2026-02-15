noss=[1,2,3,4,55,89]
def addNos(listNos):
    sum=0
    for no in listNos:
        sum=sum+no
    return sum
def susbtarct(nos):
    subs=0
    for n in nos:
        subs=subs-n
    return subs
def primeNos(nos):
    while nos>=0:
        print(nos)
        nos=nos-1

dicNos={addNos:noss,susbtarct:[10,6]}
for entry in dicNos.keys():
    tottal=entry(dicNos[entry])
    print(tottal)

