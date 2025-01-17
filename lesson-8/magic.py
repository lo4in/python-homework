class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x , self. y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.x - other. y)
    def __str__(self):
        return f'Point({self.x} ,{self.y})'

while True:
    try: 
        x1 = int(input("X1: "))
        y1 = int(input("Y1: "))
        x2 = int(input("X2: "))
        y2 = int(input("Y2: "))
                    
    except ValueError or NameError:
        print("Invalid values!")
    break        
            

    
            
       
p1 = Point(x1, y1)
p2 = Point(x2, y2)


p3 = p1 + p2
p4 = p1 - p2


print(p3)
print(p4)
