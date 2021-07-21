# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of rectangle: ", self.length*self.width)


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        print("Area of square : ", self.length*self.width)


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        print("Volume of cube: ", self.length*self.width*self.height)


# inmplementation
rectangle = Rectangle(4, 6)
rectangle.area()

square = Square(5, 5)
square.area()

cube = Cube(5, 6, 3)
cube.volume()
