name=input("please enter any string")
count=0
for i in name:
    if i in "aeiouAEIOU":
        count=count+1
print(count)