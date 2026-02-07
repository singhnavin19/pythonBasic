print("hello","sir")
print("hello")
print()
def add(*nos):
    sum=0
    for no in nos:
        sum=sum+no
    print("addition is=",sum)
add(19)
add(19,20)
add(12,3,45,6,7,8)


def addNamed(fName,lName="Singh",*nosss,**nos):
    print(fName,lName,nosss,nos)
addNamed("Navin",no=10,no2=40)
