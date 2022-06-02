from figures import Figures

class Circle(Figures):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.14 * self.radius**2
        return area

    def get_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter