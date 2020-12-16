class Person:
    def __init__(self):
        self.name = 'Aman Bansal'
        self.db = self.Dob()

    def display(self):
        print('Name:', self.name)

    class Dob:
        def __init__(self):
            self.dd = 17
            self.mm = 10
            self.yy = 1997

        def display(self):
            print(f'DOB: {self.dd}/{self.mm}/{self.yy}')


p = Person()
Person().display()
x = Person().db
x.display()
