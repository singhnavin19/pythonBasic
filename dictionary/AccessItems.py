d2={1:"Jan",2:"Feb",3:"March",4:"April","5":"May"}
print(d2)
#1. access elements form dictionary
print(d2[1])
print(d2[4])
print(d2["5"])

#2. access elements using loop
print("*"*10,"loop example start ")

for k in d2:
    print("key is :",k," and value is :",d2[k])

print("*"*10,"loop example end\n")

# 3.seperate key and value
print("*"*10,"all keys and value of dictionay start")

print(d2.keys())
print(d2.values())

print("*"*10,"all keys and value of dictionay end \n")

#to check 5 and 5.0 is same
print("*"*10,"to check 5 and 5.0 is same")
d3={5.0:"Five",5:"Five1"}
print(d3)
print("5 and 5.0 is same",5==5.0)