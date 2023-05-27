class Item:
    def __init__(self, name: str, price: float, quantity=0):
        #run validations to the received arguments
        assert price >= 0, f"price {price} must be greater than or equal to zero"
        assert quantity >= 0, f"price {quantity} must be greater than or equal to zero"

        #assignment to self objects
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)


print(item1.name, item1.price, item1.quantity)
print(item2.name, item2.price, item2.quantity)