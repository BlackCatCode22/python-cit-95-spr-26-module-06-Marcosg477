class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


a1 = Animal("Mystery")
d1 = Dog("Buddy")
c1 = Cat("Whiskers")

a1.speak()
d1.speak()
c1.speak()