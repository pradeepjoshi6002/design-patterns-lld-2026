from ShapeFactory import ShapeFactory

my_circle=ShapeFactory.create_shape("Circle",5)

my_square=ShapeFactory.create_shape("Square",10)
# print(my_circle.area(),my_circle.perimeter())

print(f"area:{my_square.area()}, perimeter: {my_square.perimeter()}")