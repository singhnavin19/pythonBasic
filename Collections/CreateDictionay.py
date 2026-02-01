# what :- 
d1={}
print(type(d1))
s={}
print(type(s))
s2=set()
print(s2)

d2=dict({"name":"navin"})
print(d2)

d3=dict(name="Navin",
        age=64,
        int=78)
print(d3)
ll=[1,2,4]
d4={1:"One","Two":2,13.67:56,45:ll}
print(d4)
ll.append(10)
print(d4)

d5=dict.fromkeys([1,2,3,4],9)
print(d5)

d6={(1,2):(3,4)}
print(d6)

d7=dict([
    (1,2),(2,1),(3,4),(8,5)
])
print(d7)

d8=dict(zip((2,3,6,7,9),(4,5,6,7,9,10)))
print(d8)
