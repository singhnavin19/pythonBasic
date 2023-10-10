#1. create tuple

t1=(1,2,3)
print(type(t1))

#2. create tuple
t2=1,2,3
print(type(t2))
#3. create tuple

t3=tuple((1,2,3))
print(type(t3))

t4=()
print(type(t4))

t5=1,
print(type(t5))

t6=tuple("hello")
print(type(t6))
print(t6[0])
print(t6[-2])

# t7=tuple(eval(input("please enter your tuple"))) in eval  you have to type entire syntax
t7=tuple(eval(input("please enter your tuple")))

print(type(t7))