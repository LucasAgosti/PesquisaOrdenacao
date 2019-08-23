import matplotlib.pyplot as plt
from random import randint
from random import shuffle
import timeit

def geraLista(size):

    arr = list(range(1, size + 1))
    shuffle(arr)

    return arr

def shellSort(lista):

    intervalo = len(lista) // 2

    while intervalo > 0:
        for index in range(intervalo, len(lista)):
            pivo = lista[index]
            aux_index = index
            while aux_index >= intervalo and lista[aux_index - intervalo] > pivo:
                lista[aux_index] = lista[aux_index - intervalo]
                aux_index = aux_index - intervalo
            lista[aux_index] = pivo
        intervalo //= 2

def showGraph(x, y, xl = "Números de elementos", yl = "Saidas", imgName = "shellSort"):
    plt.figure(figsize=(12, 16))
    plt.plot(x, y, label="Vetor aleatório {} ")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)


arr = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
aux = []

for i in arr:
    arrFinal = geraLista(i)
    aux.append(timeit.timeit("shellSort({})".format(arrFinal),
                              setup="from __main__ import shellSort", number=1))
    print(i)

showGraph(arr, aux, xl = "N de elementos", yl = "Tempo", imgName = "shellSort.png")
