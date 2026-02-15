def primeNos(nos):
    for i in range(2,nos):
        if nos%i==0:
           return "Not a Prime Number ,it divisible by "+str(i)

result=primeNos(50)
if result is None:
    print("Prime number")
else:
    print(result)

