from SA import SA
import time
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

wyniki = []
wynikiczasowe = []

def main():
    iterations = 200        #Liczba iteracji
    item_list_size = 30     #Liczba elementów
    seed = 20               # Ziarno
    init_method = 1         # Metoda wyboru rozwiązania początkowego: 1 - jedno losowe, 2 - najlepszy z 10 losowych, 3 - najelspzy ze 20 losowych
    iterationlimit = 20     # Limit iteracji
    neighbourmethod = 2     # Wybór sąsiada: 1 - wybór najlepszego sąsiada przy zamianie jednego elementu na jeden, 2 - przy zamianie jednego elementu na więcej
    temperature = 50        # Temperatura poczatkowa
    alfa = 0.98             # Zmienna przy chłodzeniu
    chill_method = 1        # Metoda chłodzenia (1-geometryczna, 2-liniowa)

    for item_list_size in range(3, 30, 5):
        for temperature in [50,70,100]:
            for chill_method in [1,2]:

                if chill_method == 1 :
                    alfa = 0.98
                else :
                    alfa = 0.05

                print("Liczba itemów "+str(item_list_size) +
                      " Temp. "+str(temperature) +
                      " Alfa "+str(alfa) +
                      " Metoda chłodzenia "+str(chill_method))
                start = time.time()
                x = SA(iterations, item_list_size, seed, init_method, iterationlimit,
                    neighbourmethod, temperature, alfa, chill_method)
                knapsack = x.solve()
                end = time.time()

                czas = end - start
                ostwynik = knapsack.get_value()
                wyniki.append(ostwynik)
                wynikiczasowe.append(czas)
                print("\nOstateczna wartość: " +
                    str(knapsack.get_value())+", czas="+str(czas))
                del x


    #print("\nW plecaku:")
    #itemlist = knapsack.get_itemlist()
    #for i in knapsack.get_itemlist():
    #    print(str(i.getId()) + " " + str(i.get_price()) + " " + str(i.get_weight()))

    argumenty = np.linspace(3, 28, 6)


    plt.plot(argumenty, wyniki[::6], label="50 - 1")
    plt.plot(argumenty, wyniki[1::6], label="50 - 2")
    plt.plot(argumenty, wyniki[2::6], label="70 - 1")
    plt.plot(argumenty, wyniki[3::6], label="70 - 2")
    plt.plot(argumenty, wyniki[4::6], label="100 - 1")
    plt.plot(argumenty, wyniki[5::6], label="100 - 2")

    plt.grid(True)
    plt.xlabel("Liczba przedmiotów (n)")
    plt.ylabel("Wynik (wartość plecaka)")
    plt.title(
        "Wykres SA wyników w zależności od temperatury i metody chłodzenia")
    plt.legend()
    plt.savefig("WykresSAWyniki.jpg", dpi=72)
    plt.show()


    plt.plot(argumenty, wynikiczasowe[::6], label="50 - 1")
    plt.plot(argumenty, wynikiczasowe[1::6], label="50 - 2")
    plt.plot(argumenty, wynikiczasowe[2::6], label="70 - 1")
    plt.plot(argumenty, wynikiczasowe[3::6], label="70 - 2")
    plt.plot(argumenty, wynikiczasowe[4::6], label="100 - 1")
    plt.plot(argumenty, wynikiczasowe[5::6], label="100 - 2")

    plt.grid(True)
    plt.xlabel("Liczba przedmiotów (n)")
    plt.ylabel("Czas [s]")
    plt.title(
        "Wykres czasu działania SA w zależności od temperatury i metody chłodzenia")
    plt.legend()
    plt.savefig("WykresSAWynikiCzasowe.jpg", dpi=72)
    plt.show()





main()
