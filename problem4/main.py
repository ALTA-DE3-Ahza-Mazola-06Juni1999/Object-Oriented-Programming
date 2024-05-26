# tulis solusi code disini
class ShippingCostCalculator:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.standard_price = 5000
        self.min_volume = 50  

    def calculate_volume(self):
        return self.length * self.width * self.height

    def calculate_cost(self):
        volume = self.calculate_volume()
        
        if volume >= self.min_volume:
            
            rounded_weight = (self.weight + 999) // 1000
            cost = rounded_weight * self.standard_price
        else:
            cost = self.standard_price  
        return cost

def main():

    length = 5
    width = 2
    height = 4
    weight = 1000 


    calculator = ShippingCostCalculator(length, width, height, weight)
    

    cost = calculator.calculate_cost()


    print(f"Harga : Rp {cost}")

if __name__ == "__main__":
    main()
