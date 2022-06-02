from figures import Figures

class Rectangle(Figures):

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def get_area(self):
        area = self.side_a * self.side_b
        return area

    def get_perimeter(self):
        perimeter = self.side_a * 2 + self.side_b * 2
        return perimeter