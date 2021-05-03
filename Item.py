

class Item:
    _weight = 0
    _price = 0
    _id = 0

    def __init__(self, id, weight, price):
        self._weight = weight
        self._price = price
        self._id = id

    def get_weight(self):
        return self._weight

    def get_price(self):
        return self._price

    def getId(self):
        return self._id