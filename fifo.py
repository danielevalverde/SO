from time import sleep
from process import Process
# https://github.com/danielevalverde/SO/blob/main/fifo.py

def run(n, list):
	list.sort(key=lambda x: x.tempo_chegada)
	tempo_espera = 0
	turnaround = 0
	start = 0
	wt = 0
	for i in range(0, n ):
		# o processo pode nao chegar no t = 0, mas ainda ser o primero processo
		start_atual = start
		if (start - list[i].tempo_chegada < 0):
			wt = 0
			start = list[i].tempo_chegada + list[i].tempo_execucao
			list[i].tempo_espera = wt
		else:
			wt = start - list[i].tempo_chegada
			start =  start + list[i].tempo_execucao
			list[i].tempo_espera = wt
		
		list[i].turnaround =  list[i].tempo_execucao + wt
		tempo_espera = list[i].tempo_execucao + tempo_espera - list[i].tempo_chegada
		turnaround = turnaround + list[i].tempo_execucao

		print('   ' * start_atual, end='')
		for j in range(0, list[i].quantun):
			sleep(1)
			print('|'+list[i].char + '|', end='', flush=True)
		print('\n')
		
	turnaround = 0
	for i in range(0, n ):
		turnaround += list[i].turnaround

	print("Average turn around time = "+  str(turnaround / n))
