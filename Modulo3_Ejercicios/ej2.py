""" Usando la clase Jet, crea nuevas instancias con los siguientes nombres y orígenes:

SU33: Russia
AJS37: Sweden
Mirage2000: France
F14: USA
Mig29: USSR
A10: USA """


class Jet:

    def __init__(self, name, country):
        self.name = name
        self.origin = country

jets_list= [
Jet("SU33", "Russia"),
Jet("AJS37", "Sweden"),
Jet("Mirage2000", "France"),
Jet("F14", "USA"),
Jet("Mig29", "USSR"),
Jet("A10", "USA")
]

for jet in jets_list:
    print(f"Nombre: {jet.name}, país: {jet.origin}")