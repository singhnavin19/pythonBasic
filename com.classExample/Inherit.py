class Student:
    def __init__(self,Fname,Lname):
        print("init method of student class called")
        self.Fname=Fname
        self.Lname=Lname
        
    def studentDetails(self):
        print(self.Fname+" "+self.Lname)    
   
class PythonStudent(Student):
    def __init__(self,xyx,lname):
        self.c=xyx
        self.d="direct"
        self.lname=lname
        print("pythonStudent")
 
# s=Student("lokesh","LokeshLastName")
# p=PythonStudent("hello","hi")
# print(p.c)
# print(p.lname)
# print(p.d)
# p.xxx="hello"
# print(p.xxx)
# p1=PythonStudent("s","s2")
# print(p1.d)


        
# s.studentDetails()            