print("rectange")
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

print("reverse")
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
