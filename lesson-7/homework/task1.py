import math

class Vectors:
  

        
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def print_data(self):
        print(self.x,self.y,self.z)

    def __add__(self, other):
        new_x = self.x + other.x 
        new_y = self.y + other.y 
        new_z = self.z + other.z
        return Vectors(new_x, new_y, new_z)

    def __sub__(self, other):

        return Vectors(self.x - other.x, self.y -self.y, self.z - self.z)

    def __mul__(self, other):
        
        return(self.x * other.x + self.y * other.y + self.z * other.z)
        

    def __rmul__(self, scalar):
        return  Vectors(self.x * scalar, self.y * scalar, self.z* 3)    
    
    
    # def __mul__(self, other):

    #     return Vectors()

    def __str__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"

    def magnitude(self):
        return ((self.x**2 + self.y**2+ self.z**2)**(1/2))

    def normalize(self):
        return Vectors(self.x/((self.x**2 + self.y**2+ self.z**2)**(1/2)), self.y/((self.x**2 + self.y**2+ self.z**2)**(1/2)), self.z/((self.x**2 + self.y**2+ self.z**2)**(1/2)))    

v1 = Vectors(1, 2, 3)
v2 = Vectors(2, 3, 4)



v1.print_data()
v2.print_data()

v3 = v1 + v2
v4 = v1 - v2
dot_product = v1 * v2
v5 = 3*v1
v_unit = v1.normalize()

print(v3)
print(v4)
print(dot_product)
print(v5)
print(round(v1.magnitude(), 2))
print(v_unit)
