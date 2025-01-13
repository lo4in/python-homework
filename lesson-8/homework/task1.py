class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says: {self.sound}"

    def eat(self, food):
        return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")

    def lay_egg(self):
        return f"{self.name} has laid an egg."

class Pig(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Oink")

    def roll_in_mud(self):
        return f"{self.name} is rolling in the mud."

# Example Usage
if __name__ == "__main__":
    # Create instances of animals
    bessie = Cow("Bessie", 5)
    clucky = Chicken("Clucky", 2)
    porky = Pig("Porky", 3)

    # Print animal behaviors
    print(bessie.make_sound())
    print(bessie.eat("grass"))
    print(bessie.produce_milk())
    print(bessie.sleep())

    print(clucky.make_sound())
    print(clucky.eat("seeds"))
    print(clucky.lay_egg())
    print(clucky.sleep())

    print(porky.make_sound())
    print(porky.eat("corn"))
    print(porky.roll_in_mud())
    print(porky.sleep())
