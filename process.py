from dataclasses import dataclass

from memory import Memory


@dataclass
class Process:
    def __init__(self, char='*', tempo_chegada=0, tempo_execucao=0, deadline=0, quantun=0, sobrecarga=0, paginas = 0, tempo_espera=0, turnaround=0, prioridade=0):
        self.char = char
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.deadline = deadline
        self.quantun = quantun
        self.sobrecarga = sobrecarga
        self.paginas = paginas
        self.tempo_espera = tempo_espera
        self.turnaround = turnaround
        self.tempo_restante = tempo_execucao
        self.prioridade = prioridade
        self.tempo_ultimo_uso = 0

    def run(self, memory: Memory):
        # chamar classe ao executar um processo para poder fazer o page_in e guardar o estado de paginação
        # (e possivelmente travar a execução do processo caso não tenha espaço na memória)

        memory.alloc(self)
        # memory.swap_in(self)

    def finish(self, memory: Memory):
        # memory.swap_out(self)
        pass

# o Tempo de chegada
# o Tempo de execução
# o Deadline
# o Quantum do sistema
# o Sobrecarga do sistema
# wt = waiting time
# ta = turning around

