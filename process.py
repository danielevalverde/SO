from dataclasses import dataclass


@dataclass
class Process:
    def __init__(self, char='*', tempo_chegada=0, tempo_execucao=0, deadline=0, quantun=0, sobrecarga=0, pagina=0, tempo_espera=0, turnaround =0, tempo_restante=0):
        self.char = char
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.deadline = deadline
        self.quantun = quantun
        self.sobrecarga = sobrecarga
        self.pagina = pagina
        self.tempo_espera = tempo_espera
        self.turnaround = turnaround
        self.tempo_restante = tempo_restante

# o Tempo de chegada
# o Tempo de execução
# o Deadline
# o Quantum do sistema
# o Sobrecarga do sistema
# wt = waiting time
# ta = turning around
