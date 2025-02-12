class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return int(3.14 *(self.radius**2))
    
    def circumference(self):
         return 2 * 3.14 * self.radius
    
r = int(input("Enter the radius of the circle :"))

C = Circle(r)
print(f"The area of the circle having {r} radius is : {C.area()}")
print(f"The circumference of the circle having {r} radius is : {C.circumference()}")