class Father:
    def __init__(self,property):
        self.property=property

    def display_property(self):
        print('Father\'s Property=',self.property)


class Son(Father):
    def __init__(self,property1,property):
        super().__init__(property)
        self.property1= property1

    def display_property(self):
        print(f'sons property is= {self.property + self.property1}')

s=Son(2000000,8000000)
s.display_property()







class Square:
    def __init__(self,x):
        self.x=x

    def area(self):
        print("area of square= {:.2f}".format(self.x*self.x))


class rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def area(self):
        super(rectangle, self).area()
        print('area of reactangle={:.2f}'.format(self.x *self.y))

a,b=[float(x) for x in input('enter two measurements= ').split()]
r=rectangle(a,b)
r.area()