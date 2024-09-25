class Calculate:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def area(self):
        if self.width is None:
            return self.length * self.length
        else:
            return self.length * self.width

class Square(Calculate):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return super().area()

class Rectangle(Calculate):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return super().area()

# Example usage:
square = Square(5)
rectangle = Rectangle(4, 6)

print(f"Area of square: {square.area()}")     # Output: Area of square: 25
print(f"Area of rectangle: {rectangle.area()}") # Output: Area of rectangle: 24
