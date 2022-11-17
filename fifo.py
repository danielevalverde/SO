from time import sleep
from process import Process

list_of_process = []


def run(n, list):
    tempo_espera = 0
    turnaround = 0
    for i in range(0, n):
        list[i].tempo_espera = int(tempo_espera)
        list[i].turnaround = int(list[i].tempo_execucao) + turnaround
        tempo_espera = int(list[i].tempo_execucao) + int(tempo_espera)
        turnaround = turnaround + int(list[i].tempo_execucao)

    tempo_espera = tempo_espera - int(list[n - 1].tempo_execucao)
    # print('---------------------------')

    print("Processes Burst time " +
          " Waiting time " +
          " Char " +
          " Turn around time")

    for i in range(0, n):
        sleep(1)
        print(" " + str(i + 1) + "\t\t" +
              str(list[i].tempo_execucao) + "\t " +
              str(list[i].tempo_espera) + "\t\t " +
              str(list[i].char) + "\t\t " +
              str(list[i].turnaround) + "\t\t ")

    print("Average waiting time = " + str(tempo_espera / n))
    print("Average turn around time = " + str(turnaround / n))
