from dataclasses import dataclass, field
from process import Process

"""
Os processos só executam se todas as suas páginas estiverem na RAM
Tendo essa regra, como isso será implementado?

Opção 1: rodar ele junto com os processos, salvar o progresso em um array e então printar no terminal tudo com um sleep.
  É uma opção pesada (por ser uma lista de listas de processos, cada index sendo um "clock" ou 1s), mas é o que pensei.
"""

@dataclass
class Memory:
    algorithm: str
    max_size: int = 50
    slots: list[Process] = field(default_factory=list)
    size: int = 0

    def has_space_for(self, process: Process):
        if (self.size + process.pagina) <= self.max_size:
            return True

        return False

    def page_in(self, process):
        self.page_out(process)
        self.slots.append(process)

    def page_out(self, process):
        if self.algorithm == 'fifo':
            self.fifo(process)
        elif self.algorithm == 'lru':
            self.lru(process)

    def fifo(self, process):
        while self.has_space_for(process) is False:
            self.slots.pop(0)

    def lru(self, process):
        self.slots.sort(key=lambda x: x.tempo_ultimo_uso)

        while self.has_space_for(process) is False:
            self.slots.pop(0)
