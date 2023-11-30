# Создайте класс Triangle. В нём пропишите 3 (метода) функции.
# Первый метод: проверка на существование треугольника по данным сторонам.
# Второй метод : нахождение площади треугольника.
# Третий метод: нахождение периметра треугольника.

import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 =side1
        self.side2 =side2
        self.side3 =side3

    def check_existence(self):
        if (self.side1 + self.side2 > self.side3) and (self.side1 + self.side3 > self.side2)and (self.side2 + self.side3 > self.side1):
            return True
        else:
            return False

    def calculate_area(self):
        if self.check_existence():
            s = (self.side1 + self.side2 + self.side3) / 2
            area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
            return area
        else:
            return "Треугольник не существует, нельзя вычислить площадь."


    def calculate_perimeter(self):
        if self.check_existence():
            perimeter = self.side1 + self.side2 + self.side3
            return perimeter
        else:

            return "Треугольник не существует, нельзя вычислить периметр."

def is_valid_side_length(side):
    try:
        float_side = float(side)
        return float_side > 0
    except ValueError:
        return False

side1 = input("Введите длину первой стороны треугольника: ")
while not is_valid_side_length(side1):
    print("Ошибка! Введите корректное число для длины стороны.")
    side1 = input("Введите длину первой стороны треугольника: ")

side2 = input("Введите длину второй стороны треугольника: ")
while not is_valid_side_length(side2):
    print("Ошибка! Введите корректное число для длины стороны.")
    side2 = input("Введите длину второй стороны треугольника: ")

side3 = input("Введите длину третьей стороны треугольника: ")
while not is_valid_side_length(side3):
    print("Ошибка! Введите корректное число для длины стороны.")
    side3 = input("Введите длину третьей стороны треугольника: ")

triangle = Triangle(side1, side2, side3)

if triangle.check_existence():
    print(f"Периметр треугольника: {triangle.calculate_perimeter()}")
    print(f"Площадь треугольника: {triangle.calculate_area()}")
else:
    print("Треугольник не существует.")
