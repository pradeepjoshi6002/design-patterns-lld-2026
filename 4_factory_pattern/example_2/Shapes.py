from ShapeInterface import Shape


class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14

    def area(self):
        return self.pi*self.radius*self.radius

    def perimeter(self):
        return 2*self.pi*self.radius

class Rectangle(Shape):

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)


class Square(Shape):

    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

    def perimeter(self):
        return 4*self.side