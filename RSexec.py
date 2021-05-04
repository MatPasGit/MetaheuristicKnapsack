from RS import *
from Knapsack import *


def main():

    iterations = 1000
    item_list_size = 24
    seed = 20
    init_method = 3

    x = RS(iterations, item_list_size, seed, init_method)
    knapsack = x.solve()
    print("KNAPSACK VALUE")
    print(knapsack.get_value())



main()
