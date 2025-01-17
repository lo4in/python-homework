class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
    def start(self):
        return print(f"Car brand: {self.brand} is starting")
    def stop(self):
        return print(f"Car brand: {self.brand} is stoping")



car = Car("Toyota", "T52", "2000")

car.display_info()

car.start()
car.stop()