def sayHello(name):
    print("Hello ",name)
# sayHello("Navin")
hello=sayHello
# hello("Navin")

list=[sayHello,"Navin",hello]
list[0]("Navin Sir")
print(list[1])
list[2]("Rana Sir")