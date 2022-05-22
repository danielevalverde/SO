from dataclasses import dataclass


@dataclass
class Process:
  def __init__(self, tc = 0, te = 0, d = 0, p = 0, q = 0, s = 0): 
    self.tc = te 
    self.te = te 
    self.d = d
    self.p = p
    self.q = q
    self.s = s
          

# o Tempo de chegada
# o Tempo de execução
# o Deadline
# o Prioridade
# o Quantum do sistema
# o Sobrecarga do sistema