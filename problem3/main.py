# tulis solusi code disini
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"


def main():
    calc = Calculator()

    operations = {
        "Penjumlahan": (calc.add, 3, 4),
        "Pengurangan": (calc.subtract, 15, 4),
        "Perkalian": (calc.multiply, 10, 10),
        "Pembagian": (calc.divide, 12, 3)
    }

    for operation_name, (operation, a, b) in operations.items():
        result = operation(a, b)
        print(f"{operation_name} : {result}")


if __name__ == "__main__":
    main()
