l=[1,2,3,7,11]
target=5;
firstNo=0;
secondNo=0;
for i in l:
    for j in l:
        remians=target-i  
        if remians == j:
            firstNo=i;
            secondNo=j
        exit
            
print(firstNo,secondNo)                    
            
# print(i,j)