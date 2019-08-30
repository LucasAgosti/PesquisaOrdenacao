import matplotlib.pyplot as plt
from random import randint
from random import shuffle
import timeit

def geraLista(size):

    arr = list(range(1, size + 1))
    shuffle(arr)

    return arr

def bucketSort(array):

    def quickSort(array, esq, direita):
      
        if esq < direita:
            pivo = randint(esq, direita)
            temp = array[direita]
            array[direita] = array[pivo]
            array[pivo] = temp

            p = partition(array, esq, direita)
            quickSort(array, esq, p - 1)
            quickSort(array, p + 1, direita)

        return array

    def partition(array, esq, direita):
      
        pivo = randint(esq, direita)
        array[direita], array[pivo] = array[pivo], array[direita]
        pivo_index = esq - 1
        
        for pos in range(esq, direita):
            if array[pos] < array[direita]:
                pivo_index = pivo_index + 1
                array[pivo_index], array[pos] = array[pos], array[pivo_index]

        temp = array[pivo_index + 1]
        array[pivo_index + 1] = array[direita]
        array[direita] = temp

        return pivo_index + 1

    maior = max(array)
    tam = len(array)
    size = maior/tam
    baldes = [[] for _ in range(tam)]

    for i in range(tam):
        j = int(array[i]/size)
        if j != tam:
            baldes[j].append(array[i])
        else:
            baldes[tam - 1].append(array[i])

    for i in range(tam):
        quickSort(baldes[i] , 0, len(baldes[i])-1)
        
    result = []

    for i in range(tam):
        result = result + baldes[i]

    return result

def showGraph(x, y, xl = "Números de elementos", yl = "Saidas", imgName = "bucketSort"):
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
    aux.append(timeit.timeit("bucketSort({})".format(arrFinal),
                              setup="from __main__ import bucketSort", number=1))
    print(i)

showGraph(arr, aux, xl = "N de elementos", yl = "Tempo", imgName = "bucketSort.png")
