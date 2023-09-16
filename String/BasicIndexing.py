name="dynamic"
index=0
print(type(name))
print(name[-2])
print(name[-4])
print(name[5])
# print(name[10]) //string index out of range
print("iterarte over string using for loop")
for i in range(0,len(name)):
    print(name[i])

print("iterarte over string using while loop")
while index<len(name)-1:
    print(name[index])
    index=index+1
print("reverse string ")
for i in range(-1,(-len(name)-1),-1):
    print(name[i],end=" ")





