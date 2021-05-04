from RS import RS, Knapsack
import copy
from numpy.random import choice
class SA(RS):

    _temperature = 50
    _iterations = 1000
    _chill_period = 0

    def __init__(self, iterations, size, seed, init_method, iterationlimit, neighbourmethod, temperature):
        self._iterations = iterations
        self._itemlist_size = size
        self._seed = seed
        self.__init_method = init_method
        self._iterationlimit = iterationlimit
        self._neighbourmethod = neighbourmethod
        self._temperature = temperature

    def iterations_to_chill(self):
        chill = self._iterations/self._temperature
        chill = int(chill)
        self._chill_period = chill

    def find_worst_neighbour(self, knapsack):
        sack = copy.deepcopy(knapsack)
        testsack = copy.deepcopy(knapsack)
        final_list = copy.deepcopy(self._itemlist)
        test_list = copy.deepcopy(self._itemlist)

        for x in test_list:
            if x[1] == False:
                continue  ## JEŚLI POZA PLECAKIEM TO PRZEBADAJ NASTEPNY ELEMENT
            else:
                x[1] = False  ##Jeśli w plecaku to usuń i znajdź najlepszego sąsiada
                sack.del_from_itemlist(x[0])

            for i in test_list:
                if i == x:
                    continue
                if i[1] == False:  # JESLI POZA PLECAKIEM TO PODMIEN
                    if sack.get_weight() + i[0].get_weight() >= self._capacity:
                        continue
                    else:
                        sack.add_to_itemlist(i[0])
                        i[1] = True
                        if sack.get_value() < testsack.get_value():  # JEŚLI LEPSZA WARTOŚĆ TO ZAPISZ
                            # print("LEPSZA WARTOSC")
                            testsack = copy.deepcopy(sack)
                            final_list = copy.deepcopy(test_list)
                        sack.del_from_itemlist(i[0])
                        i[1] = False

        self._itemlist = copy.deepcopy(final_list)
        return testsack

    def solve(self):
        self.iterations_to_chill()
        self.init_itemlist()
        knapsack = self.init_solution()


        bestknapsack = copy.deepcopy(knapsack)

        while self._iterations > 0:
            self._iterations -= 1

            chance = self._temperature / 100
            better_worst = choice([True, False], 1, [1-chance, chance])
            print(better_worst)
            if better_worst == True:
                knapsack = self.find_best_neighbour(knapsack)
            else:
                knapsack = self.find_worst_neighbour(knapsack)

            if bestknapsack.get_value() < knapsack.get_value():
                bestknapsack = copy.deepcopy(knapsack)

            if self._iterations % self._chill_period == 0:
                self._temperature -= 1
                if self._temperature < 0: ##for safety
                    self._temperature = 0

        return bestknapsack