class Item:
    discounted_price = 0.8 
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        #run validations to the received arguments
        assert price >= 0, f"price {price} must be greater than or equal to zero"
        assert quantity >= 0, f"price {quantity} must be greater than or equal to zero"

        #assignment to self  objects
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)
        

    def calculate_total_price(self):
        return  self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discounted_price

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouser", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)