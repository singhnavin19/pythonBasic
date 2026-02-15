def sayHello(no):
    if no<=10:
        print(no)
        sayHello(no+1)
        print(no)

sayHello(1)