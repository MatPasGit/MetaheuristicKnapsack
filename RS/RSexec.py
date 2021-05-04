from RS import *
from Knapsack import *


def main():

    iterations = 10000
    item_list_size = 20
    seed = 20

    x = RS(iterations,item_list_size, seed)
    knapsack = x.solve()
    print("KNAPSACK VALUE")
    print(knapsack.get_value())



main()
