from time import sleep
from process import Process

def run(n, list):
    list.sort(key=lambda x: (x.deadline, x.tempo_chegada))
    tempo_espera = 0
    turnaround = 0
    i = 0
    start = 0
    m = n
    start_atual = 0
    while(i < n):
      if(list[i].tempo_restante > 0):
          # se o tempo de exec restante > 0, significa que ainda precisa executar
          if(list[i].tempo_restante >= list[i].quantun):
              # o quantun pode ser maior que o tempo de execucao do processo ou o tempo que resta executar
              # se tiver que esperar desconta o tempo de chegada 
              if (start - list[i].tempo_chegada > 0):
                list[i].tempo_espera = start - list[i].tempo_chegada
                start = start + list[i].quantun 
              # processo chega mas nao precisa esperar
              elif(start - list[i].tempo_chegada <= 0):
                start = list[i].tempo_chegada + list[i].quantun
                list[i].tempo_espera = 0
              list[i].tempo_restante = list[i].tempo_restante - list[i].quantun
              list[i].turnaround =  list[i].quantun + list[i].tempo_espera 
              print('   ' * start, end='')
              for j in range(0, list[i].quantun):
                sleep(1)
                # caracter pra representar o estouro de deadline
                if (list[i].deadline < (start_atual + j +1)):
                    print('|-|', end='', flush=True)
                else:
                    print('|'+list[i].char + '|', end='', flush=True)
              if (list[i].tempo_restante > 0):
                # add tempo de sobrecarga 
                start +=1
                sleep(1)
                # string vazia pra representar a sobrecarga
                print('| |', end='', flush=True)
              print('\n')
              ################
              # se depois de executar até o tempo do quantun, o processo ainda precisar de mais tempo pra executar, diminui a prioridade e reordena a fila
              if(list[i].tempo_restante > 0):
                list.sort(key=lambda x: (x.deadline, x.tempo_chegada))
                i = 0
          else:
            # se tiver que esperar desconta o tempo de chegada 
            if (start - list[i].tempo_chegada > 0):
                list[i].tempo_espera = start - list[i].tempo_chegada
            # processo chega mas nao precisa esperar
            elif(tempo_espera - list[i].tempo_chegada < 0):
                list[i].tempo_espera = 0
            start = start + list[i].tempo_restante
            list[i].turnaround =  list[i].tempo_restante + list[i].tempo_espera 
            print('   ' * start, end='')
            for j in range(0, list[i].tempo_restante):
                sleep(1)
                if (list[i].deadline < (start_atual + j +1)):
                    print('|-|', end='', flush=True)
                else:
                    print('|'+list[i].char + '|', end='', flush=True)
            print('\n')
            list[i].tempo_restante = 0

      start_atual = start 
      if(list[i].tempo_restante <=0):
        i += 1
    print('\n')

    turnaround = 0
    for i in range(0, n ):
      turnaround += list[i].turnaround
    
    print("Average turn around time = " + str(turnaround / m))