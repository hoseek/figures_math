from figures import Figures

class Square(Figures):
    
    def __init__(self, side):
        self.side = side

    def get_area(self):
        area = self.side**2
        return area

    def get_perimeter(self):
        perimeter = self.side * 4
        return perimeter