from Item import *

class Knapsack:

    _value = 0
    _weight = 0
    _capacity= 100
    _itemlist = [] #INSERT ITEMS CLASS OBJECTS  HERE
    
    def __init__(self, capacity, itemlist):
        self._capacity = capacity
        self._itemlist = itemlist
        self.knapsackValue()
        self.knapsackWeight()

    def get_capacity(self):
        return self._capacity

    def add_to_itemlist(self, item):
        if isinstance(item, Item):
            self._itemlist.append(item)
            self.knapsackValue()
            self.knapsackWeight()

    def del_from_itemlist(self, item):
        if isinstance(item, Item):
            index = -1
            for x in self._itemlist:
                index+=1
                if x.getId() == item.getId():
                    self._itemlist.pop(index)
                    self.knapsackValue()
                    self.knapsackWeight()
                    


    def get_itemlist(self):
        return self._itemlist

    def get_value(self):
        return self._value

    def knapsackValue(self):
        value = 0
        for x in self._itemlist:
            value += x.get_price()
        self._value = value
        return value

    def get_weight(self):
        return self._weight

    def knapsackWeight(self):
        weight = 0
        for x in self._itemlist:
            weight += x.get_weight()
        self._weight = weight
        return weight
