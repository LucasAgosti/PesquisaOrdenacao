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

#def geraLista(arr):
    #array = list(range(1, arr + 1))
    #shuffle(array)

    #return array

def listaDec(arr):
    list = []
    while arr > 0:
        list.append(arr)
        arr -= 1
    return list

def selectionSort(array):
    ciclos = 0
    size = len(array)

    for i in range(size):

        posMin = i

        for j in range(i + 1, size):
          if(array[posMin] > array[j]):
            posMin = j
          ciclos += 1
            
        array[i], array[posMin] = array[posMin], array[i]
        #print(array)
    return ciclos

def showGraph(x, y, r, eixo, xl = "Números de elementos", yl = "Tempo", imgName = "SelectionSort"):
    fig = plt.figure(figsize=(12, 16))
    plt.plot(x, y, label="Vetor aleatório {} ".format(eixo))
    plt.plot(x, r, label="Vetor decrescente {} ".format(eixo))
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)

operacoes = []
arr = [200, 600, 2000, 4000]
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
    time.append(timeit.timeit("selectionSort({})".format(aux[i]),setup="from __main__ import selectionSort",number=1))
    timeDec.append(timeit.timeit("selectionSort({})".format(auxDec[i]),setup="from __main__ import selectionSort",number=1))
    print(i)

showGraph(arr, time, timeDec, eixo = "Tempo", imgName = 'N de iterações no laço')
#showGraph(arr, timeDec, "vetor descrescente", imgName ='N de iterações no laço')

for i in range(len(aux)):
  time2.append(selectionSort(aux[i]))
  timeDec2.append(selectionSort(auxDec[i]))

showGraph(arr, time2, timeDec2, eixo = "Trocas", imgName = 'Tempo')
