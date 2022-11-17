from memory import Memory
from process import Process
import fifo
from processor import Processor
import rr
# from sjf import sjf

n = int(input())

list_aux = []

for i in range(n):
    aux = Process()
    aux.char, aux.tempo_chegada, aux.tempo_execucao, aux.quantun = input().split(' ')
    aux.tempo_restante = aux.tempo_execucao
    list_aux.append(aux)

plist = []
# ordena processos por ordem de chegada
for i in range(n):
    aux = list_aux[i]
    aux.tempo_chegada = int(list_aux[i].tempo_chegada)
    aux.tempo_execucao = int(list_aux[i].tempo_execucao)
    aux.quantun = int(list_aux[i].quantun)
    aux.tempo_restante = int(list_aux[i].tempo_restante)
    plist.append(aux)

plist.sort(key=lambda x: x.tempo_chegada)

# algorithm = input()

# fifo.run(n, list)
rr.run(n, plist)
# processor = Processor(delay=0.5)
# memory = Memory()

# processes = sjf(list, processor)
