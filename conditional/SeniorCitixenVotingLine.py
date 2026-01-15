booth=int(input("sir aapka booth number please"))#3
age=int(input("sir aapka age"))#19
print(type(booth),type(age))
if booth>=1 and booth<=30:
    print("Yes, your are at right place")
    if age >18 and age<60:
        print("normal queue")
    elif age>60 and age<75:
        print("no queue,direct jao")
    elif age>75:
        print("Sir/Madam aap mahan ho ,ghar se vote karo") 
else:
    print("counter 2 pe jao")