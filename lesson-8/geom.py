class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return print(f"Area = {self.width*self.height}")
    def perimeter(self):
        return print(f"Perimiter = {2*(self.width+self.height)}")
    def factorise(self, const):

        self.new_width = self.width*const
        self.new_height = self.height*const
        print(f"New width: {self.new_width}, New height: {self.new_height}")

try:
    width = int(input("Input widht: "))
    height = int(input("Input heght: "))
    const = int(input("Input const: "))    
except ValueError:
    print("Invalid value")
    exit()
Rectangle1 = Rectangle(width, height)


Rectangle1.area()
Rectangle1.perimeter()
Rectangle1.factorise(const)