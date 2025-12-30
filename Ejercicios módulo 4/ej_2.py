class DisplayBase:
    def display(self):
        return f"Valores: {self.__dict__}"

class Parent1(DisplayBase):
    def __init__(self, x):
        self.x = x

class Parent2(DisplayBase):
    def __init__(self, y):
        self.y = y

class Child(Parent1, Parent2):
    def __init__(self, x, y, z):
        Parent1.__init__(self, x)
        Parent2.__init__(self, y)
        self.z = z

c = Child(10, 20, 30)

print(c.display())