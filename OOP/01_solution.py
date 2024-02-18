# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
       total_car = 0
       def __init__(self, brand,model):
              self.__brand = brand
              self.model = model
              Car.total_car += 1


       def get_brand(self):
              return self.__brand + " !"       

       def full_name(self):
              return f"{self.brand} {self.model}"
       
       def fuel_type(self):
              return "Petrol or Diesel"
       def general_description(self):
              return "Cars are maeans of transport"
       
class ElectricCar(Car):
       def __init__(self, brand, model,battery_size):
              super().__init__(brand,model)
              self.battery_size = battery_size

       def fuel_type(self):
              return "Electric charge"       

my_tesla = ElectricCar("Tesla","Model S","85KWH")
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
car = Car("Tata","Nexon")
print(safari.fuel_type())
print(safari.total_car)
print(car.general_description())



my_car = Car("Toyota","Vellfire 🔥")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_new_car = Car("Toyota","Fortuner 😎")
# print(my_new_car.brand)
# print(my_new_car.model)