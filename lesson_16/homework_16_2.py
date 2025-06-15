from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return (f"Фігура: {self.__class__.__name__}. "
                f"Периметр: {self.perimeter():.2f}. "
                f"Площа: {self.area():.2f}")


class Circle(Figure):
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

    def perimeter(self):
        return 2 * Circle.PI * self.radius


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if not self.is_valid(side_a, side_b, side_c):
            raise ValueError("Сторони не утворюють коректний трикутник!")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @staticmethod
    def is_valid(a, b, c):
        return (a + b > c) and (a + c > b) and (b + c > a)


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)


if __name__ == "__main__":
    figures = [Circle(6),
               Triangle(4, 5, 7),
               Rectangle(7, 2)]

    for fig in figures:
        print(fig)
