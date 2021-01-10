# Program 1

class Student:

    def __init__(self, n='', m=0):
        self.name = n
        self.marks = m

    def display(self):
        print('My name is=', self.name)
        print('My marks are=', self.marks)

    def calculate(self):
        if self.marks >= 600:
            print('You got first grade')
        elif self.marks >= 500:
            print('You got second grade')
        elif self.marks >= 400:
            print('You got third grade')
        else:
            print('You are fail')


n = int(input('Enter number of students='))

i = 0
while i < n:
    name = input('Enter name: ')
    marks = int(input('Enter marks: '))

    s = Student(name, marks )
    s.display()
    s.calculate()
    i += 1
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')



# Program 2 accessor and mutator methods

class Student:

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n = int(input('Enter number of students='))

i = 0
while i < n:
    s=Student()
    name = input('Enter name: ')
    s.setName(name)
    marks = int(input('Enter marks: '))
    s.setMarks(marks)
    print('Hi',s.getName())
    print('Your marks',s.getMarks())
    i += 1
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')


