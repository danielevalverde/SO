from time import sleep
from process import Process
# https://github.com/danielevalverde/SO/blob/main/fifo.py

def run(n, list):
	list.sort(key=lambda x: x.tempo_chegada)
	start = 0
	for i in range(0, n ):
		# instante em que comeca a executar para o print
		start_atual = start
		# o processo pode nao chegar no t = 0, mas ainda ser o primero processo
		if (start - list[i].tempo_chegada < 0):
			list[i].tempo_espera = 0
			start = list[i].tempo_chegada + list[i].tempo_execucao
		else:
			list[i].tempo_espera = start - list[i].tempo_chegada
			start =  start + list[i].tempo_execucao
		
		list[i].turnaround =  list[i].tempo_execucao + list[i].tempo_espera


		print('   ' * start_atual, end='')
		for j in range(0, list[i].tempo_execucao):
			sleep(1)
			print('|'+list[i].char + '|', end='', flush=True)
		print('\n')
		
	turnaround = 0
	for i in range(0, n ):
		turnaround += list[i].turnaround

	print("Average turn around time = "+  str(turnaround / n))
