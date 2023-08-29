print("square")
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print("Traingle")
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("reverse traingle")
for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

print("trainge with")
for i in range(1,6):
    for k in range(1,6-i):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="")
    print()


print("\npyramid")
for i in range(1,6):
    for k in range(1,6-i):
        print(end=" ")
    for j in range(0,2*i-1):
        print("*",end="")
    print()



print("\nreverse pyramid")
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(end=" ")
    for j in range(0,2*i-1):
        print("*",end="")
    print()

print("\n rectange ")
for i in range(0,5):
    for j in range(0,10):
        print("*",end=" ")
    print()


print("\nlast pattern")
for i in range(1,6):
    for i1 in range(0,i):
        print("*",end="")
    for j in range(0,10-2*i):
        print("",end=" ")
    for i1 in range(0,i):
        print("*",end="")
    print()

print("factorial code")
no=int(input("please enter number"))
factorial=1
if no==0:
    print(factorial)
elif no<0:
    print("negative -12number doesn't have factorial")
else:    
    for i in range(1,no+1):
            factorial=factorial*i
    print(factorial)

print("buy code")

buyCount=int(input("please enter count"))
cost=1
if buyCount<10:
    cost=buyCount*120
elif buyCount>10 and buyCount<=99:
    cost=buyCount*100
else:
    cost=buyCount*70
print(cost)