class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def intro(self):
        print(f"Hello this is the {self.brand} automobiles")
    def fullname(self):
        return f"{self.brand} {self.model}"

my_car=Car('toyota','corolla')
print(f'Brand of the Car is "{my_car.brand}"')
print(f'Model of the Car is "{my_car.model}"')
my_car.intro()

class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize=batterySize

my_tesla=ElectricCar('Tesla','Model S','85kWh')
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.batterySize)
my_tesla.intro()
print(my_tesla.fullname())