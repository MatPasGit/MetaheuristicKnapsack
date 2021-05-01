from Knapsack import *
from Item import *

class RS:

    _iterations= 100
    _itemlist = []
    _solution = []
    _itemlist_size = 20
    def __init__(self, iterations):
        self._iterations = iterations

    def init_itemlist(self):
        for x in range(0, self._itemlist_size ):
            self._itemlist.append( Item(10,20) )   #tu jakis rand cziba chyba


    def solve(self):
        self.init_itemlist()

        while self._iterations > 0 :
            self._iterations -= 1


        return ("NO SIEMA XD")