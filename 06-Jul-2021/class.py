class Student : 
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

s1 = Student("Alex",95)
s2 = Student("John",96)
print(s1.name," is Scored ",s1.mark)
print(s2.name," is Scored ",s2.mark)

class Parent : 
    def add(self,a,b) :
        self.c = a+b
        print(self.c)

class Child(Parent) : 
    pass

sum = Child()
sum.add(4,5)
