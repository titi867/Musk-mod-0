""" Añade otro atributo llamado "cantidad" a la clase. El usuario le dará valor
pasando un nuevo parámetro por el constructor. A continuación, crear 2 instancias
para: F14 y Mirage2000 con las cantidades 87 y 35. """

class Jet:

    def __init__(self, name, country, quantity):
        self.name = name
        self.origin = country
        self.quantity = quantity

jet_mirage = Jet("Mirage2000", "France", 35)
jet_f14 = Jet("F14", "USA", 87)

print(f"Nombre: {jet_f14.name}. País: {jet_f14.origin}. Cantidad: {jet_f14.quantity} unidades.")
print(f"Nombre: {jet_mirage.name}. País: {jet_mirage.origin}. Cantidad: {jet_mirage.quantity} unidades.")
    