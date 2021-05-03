from Item import *

class Knapsack:

    _value = 0
    _capacity= 100
    _itemlist = [] #INSERT ITEMS CLASS OBJECTS  HERE
    def __init__(self, capacity, itemlist):
        self._capacity = capacity
        self._itemlist = itemlist
        self.knapsackValue()

    def get_capacity(self):
        return self._capacity

    def add_to_itemlist(self, item):
        if isinstance(item, Item):
            self._itemlist.append(item)
            self.knapsackValue()

    def del_from_itemlist(self, item):
        if isinstance(item, Item):
            index = -1
            for x in self._itemlist:
                index+=1
                if x.getId() == item.getId():
                    self._itemlist.pop(index)
                    self.knapsackValue()
                    return


    def get_itemlist(self):
        return self._itemlist

    def knapsackValue(self):
        value = 0
        for x in self._itemlist:
            value += x.get_price()
        self._value = value
        return value