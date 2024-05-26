# tulis solusi code disini
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Assume this is a right-angled triangle for simplicity
        return self.base + self.height + (self.base**2 + self.height**2)**0.5


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


def main():
    shapes = {
        "Luas": [
            Square(4),
            Triangle(3, 4),
            Rectangle(7, 8)
        ],
        "Keliling": [
            Square(4),
            Triangle(3, 4),
            Rectangle(7, 8)
        ]
    }

    for calculation, shape_list in shapes.items():
        print(calculation)
        for shape in shape_list:
            if calculation == "Luas":
                print(f"{shape.__class__.__name__} : {shape.area()}")
            else:
                print(f"{shape.__class__.__name__} : {shape.perimeter()}")


if __name__ == "__main__":
    main()
