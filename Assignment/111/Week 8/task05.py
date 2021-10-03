# Task 05

class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def print_position(self):
        temp = self.x, self.y
        print(temp)
    def moveUp(self):
        self.y += 1
    def moveDown(self):
        self.y -= 1
    def moveLeft(self):
        self.x -= 1
    def moveRight(self):
        self.x += 1

car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()