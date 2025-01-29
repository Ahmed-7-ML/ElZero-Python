

class Shape(object):
    def __init__(self, length):
        self.length = length

    def calc_area(self):
        pass 
    def calc_perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def calc_area(self):
        return self.length **2
    
    def calc_perimeter(self):
        return self.length * 4


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def calc_area(self):
        return self.length *self.width
    
    def calc_perimeter(self):
        return (self.length + self.width )* 2