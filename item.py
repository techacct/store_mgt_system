import csv

class Item:
    discounted_price = 0.8 
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        #run validations to the received arguments
        assert price >= 0, f"price {price} must be greater than or equal to zero"
        assert quantity >= 0, f"price {quantity} must be greater than or equal to zero"

        #assignment to self  objects
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.discounted_price

    def apply_increment(self, increment):
        self.__price = self.__price + self.__price * increment
      
    @property
    # Prperty Decorator = Read-Only Attribute 
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 15:
            raise Exception("The name is too long")
        else:
            self.__name = new_name

    def calculate_total_price(self):
        return  self.__price * self.quantity



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
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
