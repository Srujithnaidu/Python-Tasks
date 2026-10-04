# 1.Single inheritance with polymorphism
class Robot:
    def move(self):
        print("Robot is moving")

class DancingRobot(Robot):
    def move(self):
        print("Robot is dancing")

r = Robot()
r.move()

d = DancingRobot()
d.move()

# ----------------------------------------------------------------------------

# 2.Single inheritance with polymorphism
class Teacher:
    def teach(self):
        print("Teacher is teaching")

class FunnyTeacher(Teacher):
    def teach(self):
        print("Teacher is teaching with jokes")

t = Teacher()
t.teach()

f = FunnyTeacher()
f.teach()

# ----------------------------------------------------------------------------

# 3.Multilevel inheritance with polymorphism
class Person:
    def speak(self):
        print("Person is speaking")

class Student(Person):
    def speak(self):
        print("Student is answering")

class Topper(Student):
    def speak(self):
        print("Topper is giving the answer")

p = Person()
p.speak()

s = Student()
s.speak()

t = Topper()
t.speak()

# ----------------------------------------------------------------------------

# 4.Multilevel inheritance with polymorphism
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says Bow Bow ...")

class Puppy(Dog):
    def sound(self):
        print("Puppy says Woooof ...")

a = Animal()
d = Dog()
p = Puppy()

a.sound()
d.sound()
p.sound()

# ----------------------------------------------------------------------------

# 5.Hierarchical Inheritance — Polymorphism
class Food:
    def eat(self):
        print("Eating food")

class Pizza(Food):
    def eat(self):
        print("Eating Pizza")

class Burger(Food):
    def eat(self):
        print("Eating Burger")

p = Pizza()
p.eat()

b = Burger()
b.eat()

# ----------------------------------------------------------------------------

# 6.Hierarchical Inheritance — Polymorphism
class Game:
    def play(self):
        print("Playing a game")

class Cricket(Game):
    def play(self):
        print("Playing Cricket")

class Football(Game):
    def play(self):
        print("Playing Football")

c = Cricket()
c.play()

f = Football()
f.play()

# ----------------------------------------------------------------------------

# 7.Multiple Inheritance with Polymorphism
class Chef:
    def show(self):
        print("Chef is cooking")

class Singer:
    def show(self):
        print("Singer is singing")

class Superstar(Chef, Singer):
    def show(self):
        print("Superstar is cooking and singing")

c = Chef()
c.show()

s = Singer()
s.show()

x = Superstar()
x.show()

# ----------------------------------------------------------------------------

# 8.Multiple Inheritance with Polymorphism
class Driver:
    def play(self):
        print("Driver is driving")

class Gamer:
    def play(self):
        print("Gamer is playing")

class CarGamer(Driver, Gamer):
    def play(self):
        print("Playing car racing game")

d = Driver()
d.play()

g = Gamer()
g.play()

c = CarGamer()
c.play()

# ----------------------------------------------------------------------------

#9.Hybrid Inheritance with Polymorphism (hierarchical + multiple inheritance)
class Animal:
    def sound(self):
        print("Animal makes sound")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

class Dog(Animal):
    def sound(self):
        print("Dog says Woof")

class Pet(Cat, Dog):
    def sound(self):
        print("Pet makes a cute sound")

c = Cat()
c.sound()

d = Dog()
d.sound()

p = Pet()
p.sound()

# ----------------------------------------------------------------------------

#10.Hybrid Inheritance with Polymorphism (hierarchical + multilevel inheritance)
class Device:
    def use(self):
        print("Using a device")

class Phone(Device):
    def use(self):
        print("Using a phone")

class Laptop(Device):
    def use(self):
        print("Using a laptop")

class Smartphone(Phone):
    def use(self):
        print("Using a smartphone")

d = Device()
p = Phone()
l = Laptop()
s = Smartphone()

d.use()
p.use()
l.use()
s.use()