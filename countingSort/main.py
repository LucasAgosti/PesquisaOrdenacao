import matplotlib.pyplot as plt
from random import randint
from random import shuffle
import timeit

def geraLista(size):

    arr = list(range(1, size + 1))
    shuffle(arr)

    return arr

def countingSort(lista):
  
    auxList = [0] * (max(lista) + 1)
    
    for item in lista:
        auxList[item] += 1
    i = 0
    lista.clear()
    for posItem in range(len(auxList)):
        lista.extend([posItem + 1] * auxList[posItem])

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
    aux.append(timeit.timeit("countingSort({})".format(arrFinal),
                              setup="from __main__ import countingSort", number=1))
    print(i)

showGraph(arr, aux, xl = "N de elementos", yl = "Tempo", imgName = "countingSort.png")
