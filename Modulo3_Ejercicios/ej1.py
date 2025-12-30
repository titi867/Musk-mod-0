""" Se ha definido una clase relativa al inventario de un jet imaginario. También se ha creado 
una instancia de esta clase Jet. Imprime el primer atributo de la instancia
class Jet:

    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jet("F16", "USA")
"""

class Jet:

    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jet("F16", "USA")

print(first_item.name)