import random

from Knapsack import *
from Item import *
import copy
from RandomNumberGenerator import *


class RS:

    _capacity = 0
    _iterations= 0
    _itemlist = []
    _itemlist_size = 0
    _seed = 20
    
    def __init__(self, iterations, size, seed):
        self._iterations = iterations
        self._itemlist_size = size
        self._seed = seed

    def init_itemlist(self):
        x = RandomNumberGenerator(self._seed)

        for i in range(0, self._itemlist_size):
            self._itemlist.append([Item(i, x.nextInt(1,30), x.nextInt(1,30)) , False ])
            print(str(self._itemlist[i][0].getId())+" " +
                  str(self._itemlist[i][0].get_price())+" "+
                  str(self._itemlist[i][0].get_weight()))
        ## [Item, Boolean] bolean value determines whether item is in knapsack or no

        self._capacity = x.nextInt(5*self._itemlist_size,10*self._itemlist_size)
        print(self._capacity)


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
                    if sack.get_weight() + i[0].get_weight() >= self._capacity:
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

        knapsack = Knapsack(self._capacity, [])

        ##INIT PROBLEM

        for x in self._itemlist:            
            if knapsack.get_weight() +  x[0].get_weight() >= knapsack.get_capacity() :
                break
            knapsack.add_to_itemlist( x[0] )
            x[1] = True

        bestKnapsack = copy.deepcopy(knapsack)


        while self._iterations > 0 :
            self._iterations -= 1

            knapsack = self.find_best_neighbour(knapsack) # it makes the list clean for some reason
            if knapsack.get_value() > bestKnapsack.get_value():
                print("Znaleziono lepszą kombinację przedmiotów. Wartość plecaka wynosi: "+str(knapsack.get_value()))
                bestKnapsack = copy.deepcopy(knapsack)

            if self._iterations % 30 == 0: #co iles zacznij od nowa
                for x in range(self._itemlist_size):
                    self._itemlist[x][1] = False
                random.shuffle(self._itemlist)

                knapsack = Knapsack(self._capacity, [])

                for x in self._itemlist:  ##INIT PROBLEM
                    if knapsack.get_weight() +  x[0].get_weight() >= knapsack.get_capacity() :
                        break
                    knapsack.add_to_itemlist(x[0])
                    x[1] = True

        return bestKnapsack
