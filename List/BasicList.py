#1. declare list
l=[10]
print(l)
print(type(l))

#2. empty list
l1=list()
print(l1)

l2=[1,2,3,"A",10.34]
print(l2[1])
print(l2[-1])
print(l2[1:3])
print(l2[-1:-4:-1])

nestedList=[1,2,3,[4,5]]
print(nestedList)
print(nestedList[3][0:])
print(len(nestedList))

dupList=[1,1,1]
print(dupList)
dupList[2]=20
print(dupList)

listFromSequence=list("Hello")
print(listFromSequence)

#listOfSequenceInput=list(input("pleaae enter string"))
#print(listOfSequenceInput)


#in operator
list1=[1,2]
list2=[3,4]
list3=list1+list2
print(list3)
list4=list3*2
print(list4)
