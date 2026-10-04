class Bank:
    bank_name = "State Bank of India"
    branch = "Hyderabad"
    def __init__(self, account_holder, account_number, account_type, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def display(self):
        print("Bank Name:", Bank.bank_name)
        print("Branch:", Bank.branch)
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)
        print()

customer1 = Bank("Srujith", 101, "Savings", 25000)
customer2 = Bank("Ganesh", 102, "Current", 50000)

customer1.display()
customer2.display()


# ------------------------------------------------------------------------------------------

class Movie:
    industry = "Indian Cinema"
    language = "Telugu"
    def __init__(self, name, hero, genre, rating):
        self.name = name
        self.hero = hero
        self.genre = genre
        self.rating = rating

    def display(self):
        print("Industry:", Movie.industry)
        print("Language:", Movie.language)
        print("Movie Name:", self.name)
        print("Hero:", self.hero)
        print("Genre:", self.genre)
        print("Rating:", self.rating)
        print()

movie1 = Movie("RRR", "NTR", "Action", 9.0)
movie2 = Movie("Devara", "Jr NTR", "Action", 8.0)

movie1.display()
movie2.display()


# ------------------------------------------------------------------------------------------

class Student:
    college = "IARE"
    course = "B.Tech"
    def __init__(self, name, roll_no, branch, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.cgpa = cgpa

    def display(self):
        print("College:", Student.college)
        print("Course:", Student.course)
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Branch:", self.branch)
        print("CGPA:", self.cgpa)
        print()


student1 = Student("Srujith", 101, "ECE", 7.0)
student2 = Student("Rahul", 102, "CSE", 8.2)

student1.display()
student2.display()


# ------------------------------------------------------------------------------------------

class Car:
    company = "Toyota"
    fuel_type = "Petrol"
    def __init__(self, model, color, price, mileage):
        self.model = model
        self.color = color
        self.price = price
        self.mileage = mileage

    def display(self):
        print("Company:", Car.company)
        print("Fuel Type:", Car.fuel_type)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Price:", self.price)
        print("Mileage:", self.mileage)
        print()


car1 = Car("Fortuner", "White", 4000000, 14)
car2 = Car("Innova", "Black", 3000000, 16)

car1.display()
car2.display()