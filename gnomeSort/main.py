import matplotlib.pyplot as plt
from random import randint
from random import shuffle
import timeit

def geraLista(size):

    arr = list(range(1, size + 1))
    shuffle(arr)

    return arr

def gnomeSort(arr):
  
    size = len(arr)
    x = 0
    
    while x < size:
        if x == 0:
            x = x + 1
        if arr[x] >= arr[x - 1]:
            x = x + 1
        else:
            aux = arr[x]
            arr[x] = arr[x-1]
            arr[x-1] = aux
            x = x - 1
            
    return arr

def showGraph(x, y, xl = "Números de elementos", yl = "Saidas", imgName = "gnomeSort"):
    plt.figure(figsize=(12, 16))
    plt.plot(x, y, label="Vetor aleatório {} ")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)

arr = [1000, 2000, 3000, 4000, 5000, 10000, 20000]
aux = []

for i in arr:
    arrFinal = geraLista(i)
    aux.append(timeit.timeit("gnomeSort({})".format(arrFinal),
                              setup="from __main__ import gnomeSort", number=1))
    print(i)

showGraph(arr, aux, xl = "N de elementos", yl = "Tempo", imgName = "gnomeSort.png")
