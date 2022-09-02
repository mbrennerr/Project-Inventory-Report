from collections import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.inventory = data
        self.index = 0
    
    def __next__(self):
        product = self.inventory[self.index]
        if not product:
            raise StopIteration
        self.index += 1
        return product
