from time import sleep
from process import Process
# https://github.com/danielevalverde/SO/blob/main/fifo.py
list_of_process = []

def run(n, list):
	tempo_espera = 0
	turnaround = 0
	for i in range(0, n ):

		# o processo pode nao chegar no t = 0, mas ainda ser o primero processo
		if (tempo_espera - list[i].tempo_chegada > 0):
			list[i].tempo_espera = tempo_espera - list[i].tempo_chegada
		else:
			list[i].tempo_espera = 0

		list[i].turnaround =  list[i].tempo_execucao + turnaround - list[i].tempo_chegada
		tempo_espera = list[i].tempo_execucao + tempo_espera - list[i].tempo_chegada
		turnaround = turnaround + list[i].tempo_execucao
		
	turnaround = 0
	for i in range(0, n ):
		turnaround += list[i].turnaround

	print( "Processes Tempo de exec " +
			" tempo de esp" +
			" Char " +
			" Turn around time")

	for i in range(0, n ):
		sleep(1)
		print(" " + str(i + 1) + "\t\t" +
		str(list[i].tempo_execucao) + "\t " +
		str(list[i].tempo_espera) + "\t\t " +
		str(list[i].char) + "\t\t " +
		str(list[i].turnaround) + "\t\t " )
		

	print( "Average waiting time = "+ str(tempo_espera / n))
	print("Average turn around time = "+  str(turnaround / n))
