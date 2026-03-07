class A:
    x=10
class B(A):
    pass

obj233=B()
obj233.x=0
print(obj233.x)