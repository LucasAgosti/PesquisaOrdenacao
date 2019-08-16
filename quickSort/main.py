import matplotlib.pyplot as plt
from random import randint
from random import shuffle
import timeit

def geraLista(arr):

    array = []

    while len(array) < arr:
      n = randint(1, 1 * arr)
      if n not in array: array.append(n)
    return array

def quickSort(array, esquerda, direita):
    if esquerda < direita:
        pivo = randint(esquerda, direita)
        temp = array[direita]
        array[direita] = array[pivo]
        array[pivo] = temp

        p = partition(array, esquerda, direita)
        quickSort(array, esquerda, p - 1)
        quickSort(array, p + 1, direita)

def partition(array, esquerda, direita):
    pivo = randint(esquerda, direita)

    array[direita], array[pivo] = array[pivo], array[direita]

    pivo_index = esquerda - 1
    for index in range(esquerda, direita):
        if array[index] < array[direita]:
            pivo_index = pivo_index + 1
            array[pivo_index], array[index] = array[index], array[pivo_index]

    temp = array[pivo_index + 1]
    array[pivo_index + 1] = array[direita]
    array[direita] = temp

    return pivo_index + 1

def showGraph(x, y, xl = "Números de elementos", yl = "Saidas", imgName = "quickSort"):
    fig = plt.figure(figsize=(12, 16))
    plt.plot(x, y, label="Vetor aleatório {} ")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)

arr = [100000, 200000, 400000, 500000, 1000000, 2000000]
aux = []

for i in range(len(arr)):
    arrayFinal = geraLista(i)
    aux.append(timeit.timeit("quickSort({}, {}, {})".format(arrayFinal, 0, i - 1),setup="from __main__ import quickSort",number=1))
  
    print(i)

showGraph(arr, aux)
