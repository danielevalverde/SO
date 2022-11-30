from memory import Memory
from process import Process
import fifo
from processor import Processor
import rr
import sjf
import prio
import edf

algorithm = input()
if(algorithm != "fifo" and algorithm != "sjf" ):
    n, quantun, sobrecarga = input().split(' ')
    sobrecarga = int(sobrecarga)
else:
    n, quantun= input().split(' ')

n = int(n)
quantun = int(quantun)
list_aux = []

for i in range(n):
    aux = Process()
    if(algorithm == "fifo" or algorithm == "sjf"):
        aux.char, aux.tempo_chegada, aux.tempo_execucao, aux.paginas = input().split(' ')
    elif algorithm == "roundrobim":
        aux.char, aux.tempo_chegada, aux.tempo_execucao = input().split(' ')
    else:
        aux.char, aux.tempo_chegada, aux.tempo_execucao, aux.prioridade= input().split(' ')
        aux.sobrecarga = sobrecarga
    aux.quantun = quantun
    aux.tempo_restante = aux.tempo_execucao
    list_aux.append(aux)

if(algorithm == "fifo" or algorithm == "sjf" or algorithm == "roundrobim" ):
    list = []
    for i in range(n):
        aux = list_aux[i]
        aux.tempo_chegada = int(list_aux[i].tempo_chegada)
        aux.tempo_execucao = int(list_aux[i].tempo_execucao)
        aux.quantun = int(list_aux[i].quantun)
        aux.tempo_restante = int(list_aux[i].tempo_restante)
        aux.paginas = int(list_aux[i].paginas)
        list.append(aux)
    if(algorithm == "fifo" ):
        fifo.run(n, list)
    elif(algorithm == "sjf"):
        sjf.run(n, list)
    else:
        rr.run(n,list)
elif(algorithm == "edf"):
    list = []
    for i in range(n):
        aux = list_aux[i]
        aux.tempo_chegada = int(list_aux[i].tempo_chegada)
        aux.tempo_execucao = int(list_aux[i].tempo_execucao)
        aux.quantun = int(list_aux[i].quantun)
        aux.tempo_restante = int(list_aux[i].tempo_restante)
        aux.deadline = int(list_aux[i].prioridade) #edf
        list.append(aux)
    edf.run(n, list)
elif(algorithm == "prioridade"):
    list = []
    for i in range(n):
        aux = list_aux[i]
        aux.tempo_chegada = int(list_aux[i].tempo_chegada)
        aux.tempo_execucao = int(list_aux[i].tempo_execucao)
        aux.quantun = int(list_aux[i].quantun)
        aux.tempo_restante = int(list_aux[i].tempo_restante)
        aux.prioridade = int(list_aux[i].prioridade) * (-1)
        list.append(aux)
    prio.run(n, list)

# processor = Processor(delay=0.5)
# memory = Memory()
