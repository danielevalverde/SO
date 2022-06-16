from dataclasses import dataclass


@dataclass
class Process:
    def __init__(self, char, tc=0, te=0, d=0, q=0, s=0, pg=0, wt=0, ta=0):
        self.char = char
        self.tc = tc
        self.te = te
        self.d = d
        self.q = q
        self.s = s
        self.pg = pg
        self.wt = wt
        self.ta = ta
        self.trf = te

# o Tempo de chegada
# o Tempo de execução
# o Deadline
# o Quantum do sistema
# o Sobrecarga do sistema
# wt = waiting time
# ta = turning around
