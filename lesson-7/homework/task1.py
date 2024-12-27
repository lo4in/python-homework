import math


class Point:

    def __init__(self, x, y):
      self.x = x
      self.y = y
    
    def distance(self, p2: "Point"):
        return math.sqrt((self.x - p2[0])**2 + (self.y - p2[1])**2)


p1 = Point(1, 2)
p2 = Point(4, 5)

print(p1.distance(p2))




