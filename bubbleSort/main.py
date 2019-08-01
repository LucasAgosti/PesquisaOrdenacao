import matplotlib.pyplot as plt
from random import randint
import timeit

def geraLista(size):

    array = []

    while len(array) < size:
        n = randint(1, 1 * size)
        if n not in array: array.append(n)

    return array

operacoes = []

def bubbleSort(array):
    ciclos = 0
    size = len(array)

    for i in range(size):
        for x in range(0, size - i - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                ciclos += 1

    operacoes.append(ciclos)

def showGraph(x, y, xl = "Inputs", yl = "Outputs", imgName = "img"):
    fig = plt.figure(figsize=(12, 16))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)


array = [10, 20, 50, 100]
arrBubble = []
arrTime = []

for i in range(len(array)):
  list = geraLista(i)
  arrBubble.append(timeit.timeit("bubbleSort({})".format(geraLista(array[i])), setup="from __main__ import geraLista,bubbleSort", number = 1))
  print(i)

showGraph(array, arrTime, imgName = "Tempo")
showGraph(array, operacoes, imgName = "Iterações no laço")

#for i in range(len(array)):

  #arrTime.append(bubbleSort(geraLista(array[i])))
