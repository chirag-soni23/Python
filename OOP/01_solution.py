# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
       def __init__(self, brand,model):
              self.brand = brand
              self.model = model
# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
       def full_name(self):
              return f"{self.brand} {self.model}"


my_car = Car("Toyota","Vellfire 🔥")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Toyota","Fortuner 😎")
print(my_new_car.brand)
print(my_new_car.model)