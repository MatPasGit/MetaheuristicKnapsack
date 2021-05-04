import random

from Knapsack import *
from Item import *
import randominstance
import copy
from RandomNumberGenerator import *


class RS:

    _capacity = 100
    _iterations= 100
    _itemlist = []
    _solution = []
    _itemlist_size = 20
    
    def __init__(self, iterations):
        self._iterations = iterations

    def init_itemlist(self):
        x = RandomNumberGenerator(20)
        for i in range(0, self._itemlist_size):
            self._itemlist.append([Item(i, x.nextInt(0,20), x.nextInt(0,20)) , False ])
            print(self._itemlist)
        ## [Item, Boolean] bolean value determines whether item is in knapsack or no


    def find_best_neighbour(self, knapsack):
        sack = copy.deepcopy(knapsack)
        testsack = copy.deepcopy(knapsack)
        final_list = copy.deepcopy(self._itemlist)
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
                    if sack.get_value() + i[0].get_price() > self._capacity:
                        continue
                    else:
                        sack.add_to_itemlist(i[1])
                        i[1] = True
                        if testsack.get_value() < sack.get_value(): #JEŚLI LEPSZA WARTOŚC TO ZAPISZ
                            print("LEPSZA WARTOSC")
                            testsack = copy.deepcopy(sack)
                            final_list = copy.deepcopy(test_list)
            sack = copy.deepcopy(knapsack)      # POWROC DO BADANEGO PRZYPADKU I ZBADAJ KOLEJNEGO SĄSIADA
            test_list = copy.deepcopy(self._itemlist)

        self._itemlist = copy.deepcopy(final_list)
        return testsack


    def solve(self):
        self.init_itemlist()

        knapsack = Knapsack(100, [])

        for x in self._itemlist:            ##INIT PROBLEM
            if knapsack.get_value() +  x[0].get_price() > knapsack.get_capacity() :
                break
            knapsack.add_to_itemlist( x[0] )
            x[1] = True

        bestKnapsack = copy.deepcopy(knapsack)


        while self._iterations > 0 :
            self._iterations -= 1

            knapsack = self.find_best_neighbour(knapsack) # it makes the list clean for some reason
            if knapsack.get_value() > bestKnapsack.get_value():
                print("lol")
                bestKnapsack = copy.deepcopy(knapsack)

            if self._iterations % 30 == 0: #co iles zacznij od nowa
                for x in range(0, self._itemlist_size -1 ):
                    self._itemlist[x][1] = False
                random.shuffle(self._itemlist)
                knapsack = Knapsack(100, [])

                for x in self._itemlist:  ##INIT PROBLEM
                    if knapsack.get_value() > knapsack.get_capacity():
                        break
                    knapsack.add_to_itemlist(x[0])
                    x[1] = True

        return bestKnapsack