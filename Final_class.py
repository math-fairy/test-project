# Person class 정의
class Person:
    def __init__(self,name,address):
        self.name == name
        self.address == address

    # setter
    def setName(self,name):
        self.name = name
    
    def setAddress(self,address):
        self.address = address
    
    #getter
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    #__str__ 정의
    def __str__(self):
        return '(%s,%s)' %(self.name, self.address)

#===================상속받은 Student====================

class Student(Person):
    howManyStudents = 0  #정적변수

    def __init__(self,name=None,age=0,stunum=0,hobby=''):  
            Student.howManyStudents += 1
            self.name = name   #이름
            self.age = age     #나이
            self.stunum = stunum #학번
            self.hobby = hobby   #취미
            
            
    # setter
    def setAge(self,age):
        self.age = age
    
    def setName(self,name):
        self.name = name
    
    def setStunum(self,stunum):
        self.stunum = stunum
    
    def setHobby(self,hobby):
        self.hobby = hobby

    #getter
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name

    def getStunum(self):
        return self.stunum

    def getHobby(self):
        return self.hobby
    
    #__str__ 정의
    def __str__(self):
        return '(%s,%d,%d,%s)' %(self.name,self.age,self.stunum,self.hobby)
    
    #__eq__  정의
    def __eq__(self,other):
        if isinstance(other,Student):
            if (self.name == other.name) and (self.age == other.age) and (self.stunum == other.stunum) and (self.hobby == other.hobby):
                return "이미 저장된 정보입니다"
            else:
                return "동명이인입니다"

