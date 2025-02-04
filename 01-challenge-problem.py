class Coordinate:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, initial_coordinate, width, height):
        self.initial_coordinate = initial_coordinate
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def print_coordinates(self):
        end_coordinateX = self.initial_coordinate.coordX + self.width
        end_coordinateY = self.initial_coordinate.coordY + self.height
        
        print('Starting Coordinate (X)): ' + str(self.initial_coordinate.coordX))
        print('Starting Coordinate (Y)): ' + str(self.initial_coordinate.coordY))
        print('End Coordinate (X): ' + str(end_coordinateX))
        print('End Coordinate (Y): ' + str(end_coordinateY))

    def create():
        initial_coordinate = Coordinate(50, 100)
        rectangle = Rectangle(initial_coordinate, 90, 10)    
        return rectangle


rectangle = Rectangle(initial_coordinate, 90, 10).create()

print(rectangle.get_area())

rectangle.print_coordinates()
