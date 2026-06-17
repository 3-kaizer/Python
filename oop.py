from pyexpat import model


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def year_of_birth(self):
        return 2026 - self.age

student1 = Student("Andrew", 19)
student2 = Student("Jess", 17)
student1.display()
student2.display()
print(student1.year_of_birth())

class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def display_info(self):
        print("brand:", self.brand)
        print("color:", self.color)
        print("price:", self.price)

    def show(self):
        self.display_info()

    def get_price(self):
        return self.price

class ElectricalCar(Car):
    def show(self):
        print('Electrical Car:', self.brand)
        print('The Color Is:', self.color)
        print('price:', self.price)

car1 = Car('Toyota', 'Red', 20000)
car2 = Car('Honda', 'Blue', 60000)
electricalcar1 = ElectricalCar('Tesla', 'White', 80000)

print(car1.brand)
print(car1.get_price())

car1.show()
car2.show()
electricalcar1.show()



    