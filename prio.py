from time import sleep
from process import Process

def run(n, list):
    list.sort(key=lambda x: (x.prioridade, x.tempo_chegada))
    tempo_espera = 0
    turnaround = 0
    i = 0
    start = 0
    m = n
    update = True
    while(i < n):
      print(f"char, start, list[i].tempo_restante, turnaround: prioridade {list[i].char, start,  list[i].tempo_restante, turnaround, list[i].prioridade}")
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
                aux_t = list[i].tempo_restante
                list[i].prioridade += 1 
                aux_p = list[i].prioridade
                list.sort(key=lambda x: (x.prioridade, x.tempo_chegada))
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
                print('|'+list[i].char + '|', flush=True)
            print('\n')
            list[i].tempo_restante = 0

      if(list[i].tempo_restante <=0):
        i += 1
    print('\n')
    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")
    
    turnaround = 0
    for i in range(0, n ):
      turnaround += list[i].turnaround
    
    print("utnr: " + str(turnaround))


    for i in range(0, n):
      print(" " + str(i + 1) + "\t\t" +
          str(list[i].tempo_execucao) + "\t " +
          str(list[i].tempo_espera) + "\t\t " +
          str(list[i].turnaround) + "\t\t ")

    print("Average waiting time = " + str(tempo_espera / m))
    print("Average turn around time = " + str(turnaround / m))

    # print(tempo_espera)
 