from dataclasses import dataclass


@dataclass
class Process:
  def __init__(self, tc = 0, te = 0, d = 0, p = 0, q = 0, s = 0, wt = 0, ta = 0 ): 
    self.tc = tc
    self.te = te 
    self.d = d
    self.p = p
    self.q = q
    self.s = s
    self.wt = wt
    self.ta = ta
          

# o Tempo de chegada
# o Tempo de execução
# o Deadline
# o Prioridade
# o Quantum do sistema
# o Sobrecarga do sistema
# wt = waiting time
# ta = turning around