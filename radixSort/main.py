import matplotlib.pyplot as plt
from random import randint
from random import shuffle
import timeit

def geraLista(size):

    arr = list(range(1, size + 1))
    shuffle(arr)

    return arr

def radixSort(arr):
  
    exp = 1
    maior = max(arr) if len(arr) > 2 else 0
    buckets = [[] for i in range(10)]

    while maior // exp > 0:
        for i in arr:
            buckets[(i//exp)%10].append(i)

        del arr[:]

        for i in range(len(buckets)):

            arr.extend(buckets[i])
            buckets[i] = []
        exp *= 10
    return arr

def showGraph(x, y, xl = "Números de elementos", yl = "Saidas", imgName = "radixSort"):
    plt.figure(figsize=(12, 16))
    plt.plot(x, y, label="Vetor aleatório {} ")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)

arr = [10000, 20000, 30000, 40000, 50000, 100000, 200000]
aux = []

for i in arr:
    arrFinal = geraLista(i)
    aux.append(timeit.timeit("radixSort({})".format(arrFinal),
                              setup="from __main__ import radixSort", number=1))
    print(i)

showGraph(arr, aux, xl = "N de elementos", yl = "Tempo", imgName = "radixSort.png")
