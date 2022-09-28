# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)


# Run unit tests automatically
main(module='test_module', exit=False)


def test_get_amount_inside(self):
    self.rect.set_height(10)
    self.rect.set_width(15)
    actual = self.rect.get_amount_inside(self.sq)
    expected = 6
    self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 6.')


def test_get_amount_inside_two_rectangles(self):
    rect2 = shape_calculator.Rectangle(4, 8)
    actual = rect2.get_amount_inside(self.rect)
    expected = 1
    self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 1.')


def test_get_amount_inside_none(self):
    rect2 = shape_calculator.Rectangle(2, 3)
    actual = rect2.get_amount_inside(self.rect)
    expected = 0
    self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 0.')