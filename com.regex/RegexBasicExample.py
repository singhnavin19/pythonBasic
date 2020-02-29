import re

txt = "The rain22 in Spain"
x = re.findall("[0-9]", txt)
x1 = re.search("ai", txt)
x2=re.split("ai",txt,2,8)
x3 = re.sub("\s", "9", txt)
print(x)
print(x1.span()) 
print(x1.group())
print(x1.string)#this will print an object
print(x2)
print(x3)

