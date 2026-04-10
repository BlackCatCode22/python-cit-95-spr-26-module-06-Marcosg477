class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} has been created")

    def greet(self):
        print(f"Hello, my name is {self.name}")

    def __del__(self):
        print(f"{self.name} is being destroyed")


p1 = Person("Alice")
p1.greet()

p2 = Person("Bob")
p2.greet()

# Objects will be destroyed when program ends or references removed