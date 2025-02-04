class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, initial_coordinate, width, height):
        self.initial_coordinate = initial_coordinate
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def print_coordinates(self):
        top_right = self.initial_coordinate.x + self.width
        bottom_left = self.initial_coordinate.y + self.height
        print('Starting Coordinate (X)): ' + str(self.initial_coordinate.x))
        print('Starting Coordinate (Y)): ' + str(self.initial_coordinate.y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))

def create_rectangle():
    initial_coordinate = Coordinate(50, 100)
    rectangle = Rectangle(initial_coordinate, 90, 10)    
    return rectangle


rectangle = create_rectangle()

print(rectangle.get_area())
rectangle.print_coordinates()
