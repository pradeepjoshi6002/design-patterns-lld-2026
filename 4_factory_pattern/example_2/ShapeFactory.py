from Shapes import Circle, Rectangle, Square

class ShapeFactory:

    @staticmethod
    def create_shape(shapeType, *args):

        match shapeType:
            case "Circle":
                return Circle(radius=args[0])
            case "Rectangle":
                return Rectangle(length=args[0],breadth=args[1])
            case "Square":
                return Square(side=args[0])
            case _:
                raise ValueError(f"Invalid shape type: {shapeType}")