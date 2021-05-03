from Knapsack import *
from Item import *
from random import *

class RS:

    _iterations= 100
    _itemlist = []
    _solution = []
    _itemlist_size = 20
    def __init__(self, iterations):
        self._iterations = iterations

    def init_itemlist(self):
        self._itemlist = random_instance(20,self._itemlist_size)

    def find_best_neighbour(self, solution):
        return 0


    def solve(self):
        self.init_itemlist()

        while self._iterations > 0 :
            self._iterations -= 1


        return ("NO SIEMA XD")