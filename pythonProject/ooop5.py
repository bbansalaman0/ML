class Emp:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print('ID=', self.id)
        print('Name=', self.name)
        print('Salary=', self.salary)


class Myclass:

    @staticmethod
    def mymethod(e):
        e.salary += 2000
        e.display()


e = Emp('UE151012', 'Aman Bansal', 25000)
Myclass.mymethod(e)
