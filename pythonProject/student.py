from teacher import Teacher
class Student(Teacher):
    '''this is class'''
    def setmarks(self,marks):
        self.marks=marks

    def getmarks(self):
        return self.marks

t=Student()

t.setid('UE151012')
t.setname('Aman Bansal')
t.setroll(151012)
t.setmarks(500)



print('id= ',t.getid())
print('name= ',t.getname())
print('roll= ',t.getroll())
print('marks= ',t.getmarks())