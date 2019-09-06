import matplotlib.pyplot as plt
from random import randint
from random import shuffle
import timeit

def geraLista(size):

    arr = list(range(1, size + 1))
    shuffle(arr)

    return arr
    
def heapSort(arr):
  tam = len(arr)
  
  for i in range(tam, -1, -1):
    formaHeap(arr, tam, i)
    
  for i in range(tam-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    formaHeap(arr, i, 0)
    
def formaHeap(arr, final, i):
  
  maior = i
  right = i * 2 + 2
  left = i * 2 + 1
  
  if left < final and arr[left] > arr[i]:
    maior = left
  if right < final and arr[right] > arr[maior]:
    maior = right
  if maior != i:
    arr[maior], arr[i] = arr[i], arr[maior]
    
    formaHeap(arr, final, maior)

def showGraph(x, y, xl = "Números de elementos", yl = "Saidas", imgName = "radixSort"):
    plt.figure(figsize=(12, 16))
    plt.plot(x, y, label="Vetor aleatório {} ")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)

arr = [100000, 200000, 400000, 500000, 1000000, 2000000]
aux = []

for i in arr:
    arrFinal = geraLista(i)
    aux.append(timeit.timeit("heapSort({})".format(arrFinal),
                              setup="from __main__ import heapSort", number=1))
    print(i)

showGraph(arr, aux, xl = "N de elementos", yl = "Tempo", imgName = "heapSort.png")
