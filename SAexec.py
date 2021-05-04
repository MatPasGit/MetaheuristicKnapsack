from SA import SA


def main():
    iterations = 1000
    item_list_size = 30
    seed = 20
    init_method = 3
    iterationlimit = 100
    neighbourmethod = 1
    temperature = 50
    alfa = 0.98
    chill_method = 1

    x = SA(iterations, item_list_size, seed, init_method, iterationlimit,
           neighbourmethod, temperature, alfa, chill_method)
    knapsack = x.solve()

    print("\nOstateczna wartość: " + str(knapsack.get_value()))

    print("\nW plecaku:")
    itemlist = knapsack.get_itemlist()
    for i in knapsack.get_itemlist():
        print(str(i.getId()) + " " + str(i.get_price()) + " " + str(i.get_weight()))


main()
