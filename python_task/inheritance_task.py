#1.Single Inheritance without constructor
class Sports:
    def play(self):
        print("Playing sports")
    def practice(self):
        print("Practicing sports")

class Cricket(Sports):
    def bat(self):
        print("Playing cricket")

c = Cricket()
c.play()
c.practice()
c.bat()


# 2.Single Inheritance with constructor
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def displayEmpDet(self):
        print("Employee Name =", self.name)
        print("Salary =", self.salary)

class Developer(Employee):
    def coding(self):
        print(self.name, "is coding")

d = Developer("Srujith", 50000)
d.displayEmpDet()
d.coding()


#3.Single Inheritance with constructor + super() 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print("Name =", self.name)
        print("Age =", self.age)

class Student(Person):
    def __init__(self, name, age, clg_name):
        super().__init__(name, age)
        self.clg_name =clg_name
    def displayStudent(self):
        super().displayPerson()
        print("College name: ", self.clg_name)

s = Student("Mahansh", 22, "CBIT")
s.displayStudent()


# 4.Single Inheritance with constructor + super() 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print("Name =", self.name)
        print("Age =", self.age)

class Sleeper(Person):
    def __init__(self, name, age, sleeping_hours):
        super().__init__(name, age)
        self.sleeping_hours = sleeping_hours
    def displaySleeper(self):
        super().displayPerson()
        print("Sleeping Hours =", self.sleeping_hours)

s = Sleeper("Rahul", 21, 12)
s.displaySleeper()

# -----------------------------------------------------------------------------------------------------------------------------------------

#1. Multi-level Inheritance without constructor
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Puppy(Dog):
    def play(self):
        print("Puppy is playing")

p = Puppy()
p.eat()
p.bark()
p.play()


#2.Multi-level Inheritance with constructor
class Company:
    def __init__(self, company_name):
        self.company_name = company_name
    def displayCompany(self):
        print("Company =", self.company_name)

class Mobile(Company):
    def __init__(self, company_name, model):
        self.company_name = company_name
        self.model = model
    def displayMobile(self):
        print("Model =", self.model)

class Smartphone(Mobile):
    def __init__(self, company_name, model, storage):
        self.company_name = company_name
        self.model = model
        self.storage = storage
    def displaySmartphone(self):
        print("Company =", self.company_name)
        print("Model =", self.model)
        print("Storage =", self.storage)

s = Smartphone("IQOO", "Z7 PRO", "256GB")
s.displaySmartphone()


# 3.Multi-level Inheritance with constructor + super()
class College:
    def __init__(self, college_name):
        self.college_name = college_name
    def displayCollege(self):
        print("College =", self.college_name)

class Department(College):
    def __init__(self, college_name, department):
        super().__init__(college_name)
        self.department = department
    def displayDepartment(self):
        super().displayCollege()
        print("Department =", self.department)

class Student(Department):
    def __init__(self, college_name, department, name, roll_no):
        super().__init__(college_name, department)
        self.name = name
        self.roll_no = roll_no
    def displayStudent(self):
        super().displayDepartment()
        print("Student Name =", self.name)
        print("Roll Number =", self.roll_no)

s = Student("IARE", "ECE", "Srujith", 101)
s.displayStudent()



# 4.Multi-level Inheritance with constructor + super()
class Person:
    def __init__(self, name):
        self.name = name
    def displayPerson(self):
        print("Name =", self.name)

class Foodie(Person):
    def __init__(self, name, favourite_food):
        super().__init__(name)
        self.favourite_food = favourite_food
    def displayFoodie(self):
        super().displayPerson()
        print("Favourite Food =", self.favourite_food)

class BiryaniLover(Foodie):
    def __init__(self, name, favourite_food, biryani_count):
        super().__init__(name, favourite_food)
        self.biryani_count = biryani_count
    def displayBiryaniLover(self):
        super().displayFoodie()
        print("Biryanis eaten Today =", self.biryani_count)

p = BiryaniLover("ShivaKumar", "Biryani", 3)
p.displayBiryaniLover()