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
            
        array[i], array[posMin] = array[posMin], array[i]
        ciclos += 1
        #print(array)
    operacoes.append(ciclos)

operacoes = []
arr = [200, 600, 2000, 4000]
aux = []
auxDec = []

def showGraph(x, y, r, xl = "Números de elementos", yl = "Tempo", imgName = "SelectionSort"):
    fig = plt.figure(figsize=(12, 16))
    plt.plot(x, y, label="Vetor aleatório {} ".format(r))
    plt.plot(x, y, label="Vetor decrescente {} ".format(r))
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)

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

showGraph(arr, time, timeDec, " tempo",imgName = 'N de iterações no laço')
#showGraph(arr, timeDec, "vetor descrescente", imgName ='N de iterações no laço')

for i in range(len(aux)):
  time.append(selectionSort(time2[i]))
  timeDec.append(selectionSort(timeDec2[i]))

showGraph(arr, time, timeDec, " tempo",imgName = 'N de iterações no laço')
