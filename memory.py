from dataclasses import dataclass, field
from time import sleep

"""
Os processos só executam se todas as suas páginas estiverem na RAM
Tendo essa regra, como isso será implementado?

Opção 1: rodar ele junto com os processos, salvar o progresso em um array e então printar no terminal tudo com um sleep.
  É uma opção pesada (por ser uma lista de listas de processos, cada index sendo um "clock" ou 1s), mas é o que pensei.
"""

@dataclass
class ProcessPages:
    char: str
    pages: int
    tempo_execucao: int

    def __init__(self, process):
        self.tempo_execucao = process.tempo_execucao
        self.char = process.char
        self.pages = process.paginas

@dataclass
class Memory:
    algorithm: str = 'fifo'
    max_size: int = 50
    ram_slots: list[ProcessPages] = field(default_factory=list)
    size: int = 0

    def alloc(self, process):
        self.ram_slots.append(ProcessPages(process))

    def print(self):
        time = 0

        print("Memory:")

        while len(self.ram_slots) > 0:
            pp = self.ram_slots.pop(0)

            for i in range(0, pp.tempo_execucao):
                sleep(1)
                print(f'{time}: ', end='', flush=True)
                print(f'|{pp.char}|'*pp.pages, end='', flush=True)
                print('| |'*(self.max_size-pp.pages), flush=True)
                time += 1

    def has_space_for(self, process):
        if (self.size + process.paginas) <= self.max_size:
            return True

        return False

    def swap_out(self, process):
        for i, o in enumerate(self.ram_slots):
            if o.char == process.char:
                del self.ram_slots[i]
                break

        # remove all occurrences
        # self.ram_slots = [p for p in self.ram_slots if p.char != process.char]

        self.size -= process.paginas

    def swap_in(self, process):
        if self.algorithm == 'fifo':
            self.fifo(process)
        elif self.algorithm == 'lru':
            self.lru(process)

        # self.ram_slots.append(process)

    def fifo(self, process):
        while self.has_space_for(process) is False:
            self.ram_slots.pop(0)

    def lru(self, process):
        self.ram_slots.sort(key=lambda x: x.tempo_ultimo_uso)

        while self.has_space_for(process) is False:
            self.ram_slots.pop(0)
