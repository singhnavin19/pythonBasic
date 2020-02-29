x=10
y=0
try:
    z=x/y
    print(z)
except:
    try:
        z=x/y
        print("Divide by Zero Error occured")
    except:
        print("hello")      
finally:
    print("finally")      

add=x+y
print(add)