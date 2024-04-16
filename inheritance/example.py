class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def get_age(self):
        print(f"{self.name} is {self.age} years old")

class Elephant(Animal):
    def __init__(self, name, age, trunk_length):
        super().__init__(name, age) # Calls init of Animal
        self.trunk_length = trunk_length # Extends init from Animal, adds trunk_lenght parameter for constructor

    def trumpet(self):
        print(f"{self.name} trumpets with a {self.trunk_length} meter long trunk!")

class Lion(Animal):
    # Overwrites the eat method from Animal
    def eat(self):
        print(f"{self.name} eats meat fiercely!")

    def roar(self):
        print(f"{self.name} roars!")

# Creating instances of Elephant and Lion
elephant = Elephant("Ellie", 10, 1.5)
lion = Lion("Leo", 5)

elephant.eat()
lion.eat()

elephant.get_age()
lion.get_age()

elephant.trumpet()
lion.roar()