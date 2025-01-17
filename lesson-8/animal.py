class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"im just animal I cant speak"

class Dog(Animal):
    def speak(self):
        return f"GAV gav my name is {self.name}"

class Cat(Animal):
    def speak(self):
        return f"Myau,myau my name is {self.name}" 
    

dog = Dog("Bobik")
cat = Cat("Murka")
animal = Animal("ishak")

print(dog.speak())
print(cat.speak())
print(animal.speak())
