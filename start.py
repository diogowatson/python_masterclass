class Person:
    def __init__(self,name):
        self.name = name

    def getName(self,):
        return self.name

    def setName(self,name):
        self.name = name

class Student(Person):
    def __init__(self, course):
        self.course = course

    def getCourse(self):
        return self.course

Diogo = Student("IT")
Diogo.setName("Diogo")
print("{}'s course is {}".format(Diogo.getName(),Diogo.getCourse()))

