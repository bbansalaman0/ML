# Program 1


class Student:
    def __init__(self):
        self.name = 'Aman'
        self.age = 23
        self.marks = 500

    def talk(self):
        print('Hi, I am', self.name)
        print('My age is', self.age)
        print('My marks are', self.marks)


s1 = Student()
print(s1.name)
print(s1.age)
print(s1.marks)
print("\n")
print(s1.talk())
print('\n_____________')


# Program 2

class Student:
    def __init__(self, n='', m=0):
        self.name = n
        self.marks = m

    def display(self):
        print("I'm", self.name)
        print('My marks are', self.marks)


s2 = Student()
s2.display()
print('----------------')
s3 = Student('AmanBansal', 500)
s3.display()
print()


# Program 3

class sample:
    def __init__(self):
        self.x = 10

    def modify(self):
        self.x += 1


s1 = sample()
s2 = sample()
print('x in s1=', s1.x)
print('x in s2=', s2.x)
print('\n')
s1.modify()
print('x in s1=', s1.x)
print('x in s2=', s2.x)
print('\n \n')


# Program 4

class Sample:
    x = 10

    @classmethod
    def modify(cls):
        cls.x += 1


s1 = Sample()
s2 = Sample()
print('x in s1=', s1.x)
print('x in s2=', s2.x)
print('\n')
s1.modify()
print('x in s1=', s1.x)
print('x in s2=', s2.x)
print('\n')


# Program 5

class sample:
    x = 10


print(sample.x)

sample.x += 2

print(sample.x)

print('\n')

s1 = sample()
print(s1.x)

s1.x += 3
print(s1.x)

s2 = sample()
print(s2.x)
