

class Item:
    _weight = 0
    _price = 0

    def __init__(self, weight, price):
        self._weight = weight
        self._price = price

    def get_weight(self):
        return self._weight

    def get_price(self):
        return self._price