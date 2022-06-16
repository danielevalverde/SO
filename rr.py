from time import sleep
from process import Process

list_of_process = []


def run(n, list):
    tempo_espera = 0
    turnaround = 0
    i = 0
    while(i < n):
        list[i].tempo_espera = int(tempo_espera)
        if(int(list[i].tempo_restante) > 0):
            if(int(list[i].tempo_restante) >= int(list[i].quantun)):
                # se o tempo de exec restate > quantun
                tempo_espera = int(list[i].quantun) + int(tempo_espera)
                list[i].tempo_restante = int(list[i].tempo_restante) - int(list[i].quantun)
                list[i].turnaround = int(list[i].quantun) + turnaround 
                turnaround = turnaround + int(list[i].quantun)
                # se depois de executar até o tempo do quantun, o processo ainda precisar de mais tempo pra executar, colocamos ele novamente na lista
                if(int(list[i].tempo_restante) >0): 
                  aux = Process()
                  aux.tempo_espera = list[i].tempo_espera
                  aux.tempo_execucao = list[i].tempo_execucao
                  aux.tempo_restante = list[i].tempo_restante
                  aux.quantun = list[i].quantun
                  list.append(aux)
                  n += 1
                print('   ' * list[i].tempo_espera,end='')
                for j in range(0, list[i].quantun):
                  sleep(1)
                  print('|'+list[i].char + '|',end='', flush=True)
                print('\n')
            else:
                tempo_espera = int(list[i].tempo_restante) + int (tempo_espera)
                turnaround = turnaround + int(list[i].tempo_restante)
                list[i].turnaround =  turnaround
                print('   ' * list[i].tempo_espera,end='')
                for j in range(0, list[i].tempo_restante):
                  sleep(1)
                  print('|'+list[i].char + '|', flush=True)
                print('\n')
                list[i].tempo_restante = 0
        i += 1
    print('\n')
    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")

    for i in range(0, n):
        print(" " + str(i + 1) + "\t\t" +
              str(list[i].tempo_execucao) + "\t " +
              str(list[i].tempo_espera) + "\t\t " +
              str(list[i].turnaround) + "\t\t ")

    print("Average waiting time = " + str(tempo_espera / n))
    print("Average turn around time = " + str(turnaround / n))

    # print(tempo_espera)
    # print(ta)
