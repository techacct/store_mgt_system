import csv

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as csv_file:
           reader = csv.DictReader(csv_file)
           items = list(reader)

        for item in items:
            
            Item(
            name=item.get('name'),
            price=float(item.get('price')),
            quantity=int(item.get('quantity'))
        )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

print(Item.is_integer(7))