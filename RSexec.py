from RS import *
from Knapsack import *
import time
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

wyniki = []
wynikiczasowe = []

def main():

    iterations = 200      #Liczba iteracji
    item_list_size = 30    #Liczba elementów
    seed = 20              #Ziarno
    init_method = 1        #Metoda wyboru rozwiązania początkowego: 1 - jedno losowe, 2 - najlepszy z 10 losowych, 3 - najelspzy ze 20 losowych
    iterationlimit = 20   #Limit iteracji 
    neighbourmethod = 2    #Wybór sąsiada: 1 - wybór najlepszego sąsiada przy zamianie jednego elementu na jeden, 2 - przy zamianie jednego elementu na więcej

    for item_list_size in range(3,30,5):
        #for iterations in range(200,500,100):
        for init_method in [1,2]:
            print("Liczba itemów"+str(item_list_size) +
                "Liczba iteracji"+str(iterations) +
                "Metoda poczatkowa"+str(init_method) +
                "Metoda sasiedztwa"+str(neighbourmethod))
            start = time.time()
            x = RS(iterations, item_list_size, seed,init_method, iterationlimit, neighbourmethod)
            knapsack = x.solve()
            end = time.time()

            czas = end - start
            ostwynik = knapsack.get_value()
            wyniki.append(ostwynik)
            wynikiczasowe.append(czas)
            print("\nOstateczna wartość: "+str(knapsack.get_value())+", czas="+str(czas))
            del x

    #print("\nW plecaku:")
    #itemlist=knapsack.get_itemlist()
    #for i in knapsack.get_itemlist():
    #    print(str(i.getId())+" "+str(i.get_price())+" "+str(i.get_weight()))

    argumenty = np.linspace(3,28, 6)

    #plt.plot(argumenty, wyniki[::12], label="200 - 1 - 1")
    #plt.plot(argumenty, wyniki[::6], label="200 - 1 - 2")
    #plt.plot(argumenty, wyniki[2::12], label="200 - 2 - 1")
    #plt.plot(argumenty, wyniki[1::6], label="200 - 2 - 2")
    #plt.plot(argumenty, wyniki[4::12], label="300 - 1 - 1")
    #plt.plot(argumenty, wyniki[2::6], label="300 - 1 - 2")
    #plt.plot(argumenty, wyniki[6::12], label="300 - 2 - 1")
    #plt.plot(argumenty, wyniki[3::6], label="300 - 2 - 2")
    #plt.plot(argumenty, wyniki[8::12], label="400 - 1 - 1")
    #plt.plot(argumenty, wyniki[4::6], label="400 - 1 - 2")
    #plt.plot(argumenty, wyniki[10::12], label="400 - 2 - 1")
    #plt.plot(argumenty, wyniki[5::6], label="400 - 2 - 2")
    
    plt.plot(argumenty, wyniki[::2], label="200 - 1 - 2")
    plt.plot(argumenty, wyniki[1::2], label="200 - 2 - 2")
    
    plt.grid(True)
    plt.xlabel("Liczba przedmiotów (n)")
    plt.ylabel("Wynik (wartość plecaka)")
    plt.title("Wykres RS wyników w zależności od liczby iteracji, metody poczatkowej i metody sąsiedztwa")
    plt.legend()
    plt.savefig("WykresRSWyniki.jpg", dpi=72)
    plt.show()

    argumenty = np.linspace(3, 28, 6)

    #plt.plot(argumenty, wynikiczasowe[::12], label="200 - 1 - 1")
    #plt.plot(argumenty, wynikiczasowe[::6], label="200 - 1 - 2")
    #plt.plot(argumenty, wynikiczasowe[2::12], label="200 - 2 - 1")
    #plt.plot(argumenty, wynikiczasowe[1::6], label="200 - 2 - 2")
    #plt.plot(argumenty, wynikiczasowe[4::12], label="300 - 1 - 1")
    #plt.plot(argumenty, wynikiczasowe[2::6], label="300 - 1 - 2")
    #plt.plot(argumenty, wynikiczasowe[6::12], label="300 - 2 - 1")
    #plt.plot(argumenty, wynikiczasowe[3::6], label="300 - 2 - 2")
    #plt.plot(argumenty, wynikiczasowe[8::12], label="400 - 1 - 1")
    #plt.plot(argumenty, wynikiczasowe[4::6], label="400 - 1 - 2")
    #plt.plot(argumenty, wynikiczasowe[10::12], label="400 - 2 - 1")
    #plt.plot(argumenty, wynikiczasowe[5::6], label="400 - 2 - 2")

    plt.plot(argumenty, wynikiczasowe[::2], label="200 - 1 - 2")
    plt.plot(argumenty, wynikiczasowe[1::2], label="200 - 2 - 2")

    plt.grid(True)
    plt.xlabel("Liczba przedmiotów (n)")
    plt.ylabel("Czas [s]")
    plt.title(
        "Wykres czasu działania RS w zależności od liczby iteracji, metody poczatkowej i metody sąsiedztwa")
    plt.legend()
    plt.savefig("WykresRSWynikiCzasowe.jpg", dpi=72)
    plt.show()

main()
