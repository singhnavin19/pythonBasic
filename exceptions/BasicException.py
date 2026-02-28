def mainError():
    no=0
    try:
        no =int(input("please enter a number"))
    except ValueError as e:
        print("please enter a number not character",e)
    finally:
        print("finally")
def callMainError():
    mainError()

callMainError()
print("remaining code")
