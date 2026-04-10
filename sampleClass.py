class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


# Create objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model Y", 2022)

car1.display_info()
car2.display_info()