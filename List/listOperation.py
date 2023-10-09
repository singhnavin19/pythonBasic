#extend adding element
l1=[1,2]
l2=[3,4]
l1.extend(l2)
print(l1) #o/p= [1, 2, 3, 4]
#l1.extend(30) #give error



#append
t1=['A','B']
t2=['c','d']
t1.append(t2)
print(t1) #o/p =  ['A', 'B', ['c', 'd']]

#insert
l1=[1,3,5]
l1.insert(1,2)
print(l1)  #0/p = [1, 2, 3, 5]
l1.insert(len(l1),30) # here insert act as append or exten
print(l1)

#pop
print(20*"#","pop",20*'#')
l=[1,3,5,7,9]
l.pop(2)
print(l) #[1,3,7,9]
l.pop()
print(l)

#remove
print(20*"#","remove",20*'#')
l=[1,2,3,4,5,6]
l.remove(4)
print(l) # o/p =[1, 2, 3, 5, 6]

#clear
print(20*"#","clear",20*'#')
l=[1,2,3,4]
print("list before l.clear() =",l)
l.clear()
print("list after l.clear()= ",l)
del l
#print(l)

#count
print(20*"#","count",20*'#')
l=[1,2,3,4,2,2]
print("count of 2 in list uisng l.count(2)=",l.count(2))

#reverse
print(20*"#","reverse",20*'#')
l=[1,2,3,4,2,5]
print("before reverse=",l)
l.reverse()
print("after reverse=",l)

#sort and sorted
print(20*"#","sort and sorted",20*'#')
l=[1,2,5,3,9,8]
print("list before l.sort()=",l)
l1=l.sort()
print("list after l.sort()=",l)

l3=[1,3,5,4,9,2]
l4=sorted(l3)
print(l4)

#min max and sum

list1=[1,2,3,4]
print(min(list1))
print(max(list1))
print(sum(list1))






