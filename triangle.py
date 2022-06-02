from figures import Figures

class Triangle(Figures):
    
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        area = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))**0.5
        return area

    def get_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter