for i  in range(5):
    for j in range(5):
        print("*",end=" ")
    print() 

print("************")
no=1
for i  in range(4):
    for j in range(4):
        print(no,end=" ")
        no=no+1
    print() 
print("************")

for i  in range(4):
    no=1
    for j in range(4):
        print(no,end=" ")
        no=no+1
    print() 

for i in range(5):
    for j in range(0,i):
        print("*",end=" ")
    print("")
print("reverse")
for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("")

print("traingle")
for row in range(1,6):
    for space in range(1,6-row):
        print(end=" ")
    for col in range(1,row+1):
        print("*",end=" ")
    print("")



