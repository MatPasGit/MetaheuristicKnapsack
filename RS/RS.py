from Knapsack import *
from Item import *
from random import *
import copy

class RS:

    _capacity = 100
    _iterations= 100
    _itemlist = []
    _solution = []
    _itemlist_size = 20
    def __init__(self, iterations):
        self._iterations = iterations

    def init_itemlist(self):
        self._itemlist = [random_instance(20,self._itemlist_size), False ]
        ## [Item, Boolean] bolean value determines whether item is in knapsack or no


    def find_best_neighbour(self, knapsack):
        sack = copy.deepcopy(knapsack)
        testsack = copy.deepcopy(knapsack)
        final_list = []
        test_list = copy.deepcopy(self._itemlist)
        for x in test_list:
            if x[1] == False:
                continue    ## JEŚLI POZA PLECAKIEM TO PRZEBADAJ NASTEPNY ELEMENT
            else:
                x[1] = False        ##Jeśli w plecaku to usuń i znajdź najlepszego sąsiada
                sack.del_from_itemlist(x[0])

            for i in test_list:
                if i == x:
                    continue
                if i[1] == False:       #JESLI POZA PLECAKIEM TO PODMIEN
                    if sack.get_value() + i[1].get_price() > self._capacity:
                        continue
                    else:
                        sack.add_to_itemlist
                        i[1] = True
                        if testsack.get_value() < sack.get_value(): #JEŚLI LEPSZA WARTOŚC TO ZAPISZ
                            testsack = copy.deepcopy(sack)
                            final_list = copy.deepcopy(test_list)
            sack = copy.deepcopy(knapsack)      # POWROC DO BADANEGO PRZYPADKU I ZBADAJ KOLEJNEGO SĄSIADA
            test_list = copy.deepcopy(self._itemlist)

        self._itemlist = final_list
        return testsack


    def solve(self):
        self.init_itemlist()

        knapsack = Knapsack(100, [])

        for x in self._itemlist:            ##INIT PROBLEM
            if knapsack.get_value() > knapsack.get_capacity() :
                break
            knapsack.add_to_itemlist( x[0] )
            x[1] = True

        bestKnapsack = copy.deepcopy(knapsack)


        while self._iterations > 0 :
            self._iterations -= 1

            knapsack = self.find_best_neighbour(knapsack)
            if knapsack.get_value() > bestKnapsack.get_value():
                bestKnapsack = copy.deepcopy(knapsack)


        return bestKnapsack