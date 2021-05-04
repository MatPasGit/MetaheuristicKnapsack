import copy
from numpy.random import choice
import random
from Knapsack import *
from Item import *
from RandomNumberGenerator import *

class SA():

    _temperature = 50
    _iterations = 1000
    _chill_period = 0
    _capacity = 0
    _itemlist = []
    _itemlist_size = 0
    _seed = 20
    __init_method = 1
    _iterationlimit = 30
    _neighbourmethod = 1
    _alfa = 0.95
    _chill_method = 1

    def __init__(self, iterations, size, seed, init_method, iterationlimit, neighbourmethod, temperature, alfa, chill_method):
        self._iterations = iterations
        self._itemlist_size = size
        self._seed = seed
        self.__init_method = init_method
        self._iterationlimit = iterationlimit
        self._neighbourmethod = neighbourmethod
        self._temperature = temperature
        self._alfa = alfa
        self._chill_method = chill_method

    def init_itemlist(self):
        x = RandomNumberGenerator(self._seed)

        for i in range(0, self._itemlist_size):
            self._itemlist.append(
                [Item(i, x.nextInt(1, 30), x.nextInt(1, 30)), False])
            #print(str(self._itemlist[i][0].getId())+" " +
            #      str(self._itemlist[i][0].get_price())+" " +
            #      str(self._itemlist[i][0].get_weight()))
        ## [Item, Boolean] bolean value determines whether item is in knapsack or no

        self._capacity = x.nextInt(
            5*self._itemlist_size, 10*self._itemlist_size)
        #print(self._capacity)

    def init_solution(self):
        #print("Wybrano metode początkową: "+str(self.__init_method))

        knapsack = Knapsack(self._capacity, [])

        if self.__init_method == 1:
            for x in self._itemlist:
                if knapsack.get_weight() + x[0].get_weight() >= knapsack.get_capacity():
                    break
                knapsack.add_to_itemlist(x[0])
                x[1] = True
            return knapsack

        if self.__init_method == 2:
            bestKnapsack = 0
            for i in range(10):
                for x in self._itemlist:
                    if knapsack.get_weight() + x[0].get_weight() >= knapsack.get_capacity():
                        break
                    knapsack.add_to_itemlist(x[0])
                    x[1] = True
                if i == 0:
                    bestKnapsack = copy.deepcopy(knapsack)
                    #print("Znaleziono lepszy początek" +
                    #      str(bestKnapsack.get_value()))
                else:
                    if bestKnapsack.get_value() < knapsack.get_value():
                        bestKnapsack = copy.deepcopy(knapsack)
                    #    print("Znaleziono lepszy początek" +
                    #          str(bestKnapsack.get_value()))
                knapsack = Knapsack(self._capacity, [])
                random.shuffle(self._itemlist)
            return bestKnapsack

        if self.__init_method == 3:
            bestKnapsack = 0
            for i in range(100):
                for x in self._itemlist:
                    if knapsack.get_weight() + x[0].get_weight() >= knapsack.get_capacity():
                        break
                    knapsack.add_to_itemlist(x[0])
                    x[1] = True
                if i == 0:
                    bestKnapsack = copy.deepcopy(knapsack)
                    #print("Znaleziono lepszy początek" +
                    #      str(bestKnapsack.get_value()))
                else:
                    if bestKnapsack.get_value() < knapsack.get_value():
                        bestKnapsack = copy.deepcopy(knapsack)
                        #print("Znaleziono lepszy początek" +
                        #      str(bestKnapsack.get_value()))
                knapsack = Knapsack(self._capacity, [])
                random.shuffle(self._itemlist)
            return bestKnapsack


    def find_neighbour(self, knapsack):
        sack = copy.deepcopy(knapsack)
        testsack = copy.deepcopy(knapsack)
        final_list = copy.deepcopy(self._itemlist)
        test_list = copy.deepcopy(self._itemlist)

        random.shuffle(test_list)

        for x in test_list:
            if x[1] == False:
                continue  # JEŚLI POZA PLECAKIEM TO PRZEBADAJ NASTEPNY ELEMENT
            else:
                # Jeśli w plecaku to usuń i znajdź najlepszego sąsiada
                x[1] = False
                sack.del_from_itemlist(x[0])
                break

        for i in test_list:
            if i == x:
                continue
            if i[1] == False:  # JESLI POZA PLECAKIEM TO PODMIEN
                if sack.get_weight() + i[0].get_weight() >= self._capacity:
                    continue
                else:
                    sack.add_to_itemlist(i[0])
                    i[1] = True
                    testsack = copy.deepcopy(sack)
                    final_list = copy.deepcopy(test_list)

        return testsack, final_list

    def temperature_chill(self):
        if self._chill_method == 1 :
            self._temperature = self._temperature *self._alfa

        if self._chill_method == 2 :
            self._temperature = self._temperature - self._alfa

    def solve(self):
        self.init_itemlist()
        knapsack = self.init_solution()

        bestknapsack = copy.deepcopy(knapsack)

        while (self._iterations > 0) and (self._temperature > 0.005):
            
            self._iterations -= 1

            tempknapsack, templist = self.find_neighbour(knapsack)

            chance = math.exp((-tempknapsack.get_value()-knapsack.get_value())/self._temperature)
            better_worst = choice([True, False], 1, [1-chance, chance])
            
            if better_worst == True:
                self._itemlist = copy.deepcopy(templist)
                knapsack = copy.deepcopy(tempknapsack)

            if bestknapsack.get_value() < knapsack.get_value():
                #print("Znaleziono lepszą kombinację przedmiotów. Wartość plecaka wynosi: "+str(knapsack.get_value()))
                bestknapsack = copy.deepcopy(knapsack)

            if self._iterations % self._iterationlimit == 0:  # co iles zacznij od nowa
                for x in range(self._itemlist_size):
                    self._itemlist[x][1] = False
                random.shuffle(self._itemlist)

                knapsack = Knapsack(self._capacity, [])

                for x in self._itemlist:  # INIT PROBLEM
                    if knapsack.get_weight() + x[0].get_weight() >= knapsack.get_capacity():
                        break
                    knapsack.add_to_itemlist(x[0])
                    x[1] = True

            self.temperature_chill()
            #print(self._temperature)

        return bestknapsack
