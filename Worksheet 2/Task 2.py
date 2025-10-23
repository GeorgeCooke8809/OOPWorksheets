class Length:
    def __init__(self, length):
        self.l = length

    def length(self):
        return self.l
    
class Breadth:
    def __init__(self, width):
        self.b = width

    def breadth(self):
        return self.b
    
class Rect_Area(Length, Breadth):
    def __init__(self, width, length):
        Length.__init__(self, length)
        Breadth.__init__(self, width)

    def r_area(self):
        print(f"The area of the rectangle with length {self.length()} and width {self.breadth()} is {self.length() * self.breadth()}")

rect = Rect_Area(10, 20)
rect.r_area()