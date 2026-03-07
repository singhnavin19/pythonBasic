class AgeException(Exception):
    pass


age=int(input("please enter your age"))
if age<10:
    raise AgeException()
