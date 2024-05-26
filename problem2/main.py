# tulis solusi code disini
class Solid:
    def volume(self):
        pass


class Cube(Solid):
    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3


class RectangularPrism(Solid):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


class Cylinder(Solid):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        pi = 22 / 7  # Approximation of pi
        return pi * self.radius ** 2 * self.height


def main():
    solids = {
        "Volume": [
            Cube(10),
            RectangularPrism(3, 6, 10),
            Cylinder(7, 10)
        ]
    }

    for calculation, solid_list in solids.items():
        print(calculation)
        for solid in solid_list:
            print(f"{solid.__class__.__name__} : {solid.volume()}")


if __name__ == "__main__":
    main()
