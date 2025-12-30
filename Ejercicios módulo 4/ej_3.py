class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:' , self.name, self.color, self.price)
    
    def max_speed(self):
        print('Vehicle max speed is 15')
    
    def change_gear(self):
        print('Vehicle change 6 gear')
        
class Car(Vehicle):
    def __init__(self, name, color, price, max_speed, change_gear):
        super().__init__(name, color, price)
        self.max_speed_value = max_speed
        self.change_gear_value = change_gear
    
    def max_speed(self):
        print('Car max speed is', self.max_speed_value)

    def change_gear(self):
        print('Car change gear is', self.change_gear_value)


car = Car('Toyota', 'White', 20000, '140km/h', 6)

car.show()
car.max_speed()
car.change_gear()