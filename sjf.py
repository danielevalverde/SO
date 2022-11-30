from time import sleep

from memory import Memory
from process import Process

def run(n, list):
	list.sort(key=lambda x: (x.tempo_chegada, x.tempo_execucao))
	start = 0
	memory = Memory()

	for i in range(0, n ):
		# o processo pode nao chegar no t = 0, mas ainda ser o primero processo
		start_atual = start

		if (start - list[i].tempo_chegada < 0):
			list[i].tempo_espera = 0
			start = list[i].tempo_chegada + list[i].tempo_execucao
		else:
			list[i].tempo_espera = start - list[i].tempo_chegada
			start =  start + list[i].tempo_execucao
		
		list[i].turnaround =  list[i].tempo_execucao + list[i].tempo_espera

		memory.alloc(list[i])

		print('   ' * start_atual, end='')
		for j in range(0, list[i].tempo_execucao):
			sleep(1)
			print('|'+list[i].char + '|', end='', flush=True)
		print('')
		
	turnaround = 0
	for i in range(0, n ):
		turnaround += list[i].turnaround

	print("Average turn around time = "+  str(turnaround / n))

	print('\n')
	memory.print()
