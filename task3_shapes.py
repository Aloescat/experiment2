import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")
    
    def __gt__(self, other):
        return self.area() > other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def perimeter_gt(self, other):
        return self.perimeter() > other.perimeter()
    
    def perimeter_lt(self, other):
        return self.perimeter() < other.perimeter()

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        hypotenuse = math.sqrt(self.base**2 + self.height**2)
        return self.base + self.height + hypotenuse

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    square = Square(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4)
    circle = Circle(2)
    
    print("Square area:", square.area())
    print("Rectangle area:", rectangle.area())
    print("Square > Rectangle (area)?", square > rectangle)
    
    print("Rectangle perimeter:", rectangle.perimeter())
    print("Circle perimeter:", circle.perimeter())
    print("Rectangle > Circle (perimeter)?", rectangle.perimeter_gt(circle))
    
    print("Triangle < Circle (area)?", triangle < circle)
    print("Triangle < Circle (perimeter)?", triangle.perimeter_lt(circle))