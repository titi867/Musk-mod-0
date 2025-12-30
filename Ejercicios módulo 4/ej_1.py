class Staff:
    def __init__(self, role, deputy_salary):
        self.role = role
        self.deputy_salary = deputy_salary

    def get_role(self):
        return self.role

    def get_deputy_salary(self):
        return self.deputy_salary


class Profesor(Staff):
    def __init__(self, role, deputy_salary, name, age):
        super().__init__(role, deputy_salary)
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

prof = Profesor("Docente", 2500, "Justina", 39)

print(f"Role: {prof.get_role()}, Deputy Salary: {prof.get_deputy_salary()}, "
      f"Name: {prof.get_name()}, Age: {prof.get_age()}")