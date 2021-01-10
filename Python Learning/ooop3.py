class bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        print(f'{name} flies with {cls.wings}')

print(bird.fly)
bird.fly('Sparrow')
bird.fly('Piegon')


print()
print()
print()
print()




class Myclass:
    n=0

    def __init__(self):
        Myclass.n=Myclass.n+1

    @staticmethod
    def noObject():
        print('No of instance created:',Myclass.n)

obj1=Myclass()
obj2=Myclass()
obj3=Myclass()
obj4=Myclass()
Myclass.noObject()
