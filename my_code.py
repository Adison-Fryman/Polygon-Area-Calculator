import math


class Rectangle:

    def __init__(self, width,height):
        self.height = height
        self.width = width
        self.area = width * height
        self.diagonal = (width ** 2 + height ** 2) ** (1 / 2)
        self.perimeter = (2 * width + 2 * height)

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width


    def set_height(self, new_height):
        self.height = new_height


    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter

    def get_diagonal(self):
        return self.diagonal

    def get_picture(self):
        width = ('*' * self.width) + '\n'
        if self.width < 50:
            picture = width * self.height
            return picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, height, width):
        temp_width = 0
        temp_height = 0
        temp_rectangle = temp_width * temp_height
        how_many_widths = math.round(self.width / temp_width)
        how_many_heights = math.round(self.height / temp_height)
        return how_many_heights + how_many_widths
    #some how I need to make this take in a shape not the attributes of a shape.

class Square(Rectangle):

    def __init__(self, side_length):
        #self.Rectangle.height = side_length
        super().__init__(width=side_length, height=side_length)
        self.side_length = side_length

    def __repr__(self):
        return f'Square(side={self.side_length})'

    def set_side(Rectangle, new_side):
        Rectangle.side_length = new_side


#Rectangle
# rec1 = Rectangle(4,7)

# print(rec1.get_picture())

#squ1 = Square(51)
#print(squ1.get_picture())

#print(squ1.get_area())
#print(squ1)
#squ1.set_side(2)
#print(squ1)
#print(squ1.get_area())
#print(squ1.get_picture())
#print(squ1.get_diagonal())