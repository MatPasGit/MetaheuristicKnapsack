from RS import *
from Knapsack import *


def main():
    x = RS(10000)
    knapsack = x.solve()
    print("KNAPSACK VALUE")
    print(knapsack. get_value())



main()