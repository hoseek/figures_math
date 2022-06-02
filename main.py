from square import Square
from triangle import Triangle
from rectangle import Rectangle
from circle import Circle

def main():

    while True:
        
        figure_name = input('What figure do you need: \n')

        if figure_name == 'square':
            side = int(input('Type a side value: \n'))
            figure = Square(side)
            break

        elif figure_name == 'rectangle':
            side_a = int(input('Type side a: \n'))
            side_b = int(input('Type side b: \n'))
            figure = Rectangle(side_a, side_b)
            break

        elif figure_name == 'triangle':
            side_a = int(input('Type side a: \n'))
            side_b = int(input('Type side b: \n'))
            side_c = int(input('Type side c: \n'))
            figure = Triangle(side_a, side_b, side_c)
            break

        elif figure_name == 'circle':
            radius = int(input('Type a radius: \n'))
            figure = Circle(radius)
            break
            
        else:
            print('This figure does not exist')


    while True:

        operation_name = input('What operation do you need: \n')

        if operation_name == 'area':
            figure.print_area()
            break

        elif operation_name == 'perimeter':
            figure.print_perimeter()
            break

        else:
            print ('This operation does not exist')

if __name__ == '__main__':
    main()