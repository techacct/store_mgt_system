from item import Item

class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #call the super function to have access to all attributes/methods
        super().__init__(name, price, quantity)

        #run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be greater than or equal to zero"

        #assignment to self  objects
        self.broken_phones = broken_phones
