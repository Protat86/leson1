# test_get_area_rectangle.py: Наш код для тестирования
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

# Тестовый класс для Rectangle
class TestGetAreaRectangle:

    def test_normal_case(self):
        rectangle = Rectangle(2, 3)
        assert rectangle.get_area() == 6, "неправильная площадь для обычного случая"

    def test_negative_case(self):
        rectangle = Rectangle(-1, 2)
        
        try:
            area = rectangle.get_area()
            assert area >= 0, "неправильная площадь для отрицательного случая"
        except AssertionError as e:
            print("AssertionError: неправильный негативный результат")
        else:
            assert False, "AssertionError не был вызван для отрицательного случая"


