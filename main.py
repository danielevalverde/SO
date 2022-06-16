from process import Process
import fifo
from processor import Processor
import rr
from sjf import sjf

n = int(input())

list_aux = []

for i in range(n):
    aux = Process()
    aux.tc, aux.te, aux.qa = input().split(' ')
    list_aux.append(aux)

list = []

for i in range(n):
    aux = Process()
    print(list_aux[i].tc)
    aux.tc = int(list_aux[i].tc)
    aux.te = int(list_aux[i].te)
    aux.qa = int(list_aux[i].qa)
    list.append(aux)

list.sort(key=lambda x: x.tc)

# for i in range(n):
#   print(list[i].tc)
#   print(list[i].te)

# algorithm = input()

print('\n')

# fifo.run(n, list)
# rr.run(n, list)
