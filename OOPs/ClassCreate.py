from os import name


class Navin:

    name="Navin Singh"
    @classmethod
    def classMethodsayByeBye(clas,sjhd):
        print("ByeBye",name,sjhd)
    def __init__(self):
        print("I am constructor")
    def sayHello(self,fname,lname):
        print("Hello",fname,lname)


Navin.classMethodsayByeBye("ff")
# obj1=Navin()
# obj1.sayHello("navin","singh")
# print(obj1.name)
# obj2=Navin()
# obj1.name="Praveen Singh"
# print(obj1.name)
# print(obj2.name)