import math


class Rectangle:

    def __init__(self, width,height):
        self.height = height
        self.width = width

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
         return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** (1 / 2)

    def get_picture(self):
        width = ('*' * self.width) + '\n'
        if self.width < 50 and self.height < 50:
            picture = width * self.height
            return picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):

        how_many_widths = (self.width // shape.width)
        how_many_heights = (self.height // shape.height)
        return how_many_heights * how_many_widths


class Square(Rectangle):

    def __init__(self, side_length):
        self.height = side_length
        self.width = side_length

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side):
       self.width = new_side
       self.height = new_side




