d1={1:"One",2:"two",3:"Three",4:"Four"}
print(d1[1])

print("1.","*"*10,"Get method start")
print(d1.get(2,"Not present")) #Two
print(d1.get(20))             #none
print(d1.get(20,"Not present")) #Not present
print("1.","*"*10,"Get method end\n")


print("2.","*"*10,"items method start")
print(d1.items())
for item in d1.items():
    print(item)
for k,v in d1.items():
     print("key=",k,"value=",v)
print("2.","*"*10,"items method end \n")

print("3.","*"*10,"keys method start")
print(d1.keys())
print("3.","*"*10,"keys method end \n")

print("4.","*"*10,"values method start")
print(d1.values())
print("4.","*"*10,"values method end \n")

print("5.","*"*10,"fromkeys method start")
d2=dict.fromkeys("hello",10)
print(d2)
print("5.","*"*10,"fromkeys method end \n")
