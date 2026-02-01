studentnNames=['Priti','Shalini','Reshma','Piyush']
# print(studentnNames[0])
studentnNames[0]='Abhishek' #mutable
print(studentnNames[-3:-1]) #slice(start:end:step) start=0 end=last step
studentnNames[0:2]=['bhaumik','Vikas']
print(studentnNames)
studentnNames.append('Navin')
print(studentnNames)
for name in studentnNames:
    print(name)