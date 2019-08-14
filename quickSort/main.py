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

def listaDec(arr):
    list = []
    while arr > 0:
        list.append(arr)
        arr -= 1
    return list

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

def showGraph(x, y, r, eixo, xl = "Números de elementos", yl = "Tempo", imgName = "insertionSort"):
    fig = plt.figure(figsize=(12, 16))
    plt.plot(x, y, label="Vetor aleatório {} ".format(eixo))
    plt.plot(x, r, label="Vetor decrescente {} ".format(eixo))
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)

operacoes = []
arr = [10000, 20000, 50000, 100000]
aux = []
auxDec = []

for i in arr:
  list = geraLista(i)
  aux.append(geraLista(i))
  auxDec.append(listaDec(i))

time =[]
timeDec = []
time2 =[]
timeDec2 = []

for i in range(len(aux)):
    time.append(timeit.timeit("insertionSort({})".format(aux[i]),setup="from __main__ import insertionSort",number=1))
    timeDec.append(timeit.timeit("insertionSort({})".format(auxDec[i]),setup="from __main__ import insertionSort",number=1))
    print(i)

showGraph(arr, time, timeDec, eixo = "Tempo", imgName = 'Tempo')

for i in range(len(aux)):
  time2.append(insertionSort(aux[i]))
  timeDec2.append(insertionSort(auxDec[i]))

showGraph(arr, time2, timeDec2, eixo = "Trocas", yl = 'Iterações', imgName = 'N de iterações no laço')
