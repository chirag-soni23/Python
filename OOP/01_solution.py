# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
       def __init__(self, brand,model):
              self.__brand = brand
              self.model = model


       def get_brand(self):
              return self.__brand + " !"       
# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
       def full_name(self):
              return f"{self.brand} {self.model}"
# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
class ElectricCar(Car):
       def __init__(self, brand, model,battery_size):
              super().__init__(brand,model)
              self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85KWH")
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.get_brand())


my_car = Car("Toyota","Vellfire 🔥")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Toyota","Fortuner 😎")
print(my_new_car.brand)
print(my_new_car.model)