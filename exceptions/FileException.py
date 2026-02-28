try:
    file=open("BasicException.py",'r')
    print(file.read())
    # print(int("navin"))
    print("Navin")
    raise ValueError("Navin")
except (FileNotFoundError,ValueError) as e:
    print("file not found")
except ZeroDivisionError:
    print("division by zero")

# else:
#     print("file found")
finally:
    print("file closed")