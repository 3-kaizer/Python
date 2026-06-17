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