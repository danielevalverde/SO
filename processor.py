from dataclasses import dataclass, field
from time import sleep
from memory import Memory

from mmu import MemoryManagementUnit
from process import Process


@dataclass
class Processor:
    # overload: int

    def __init__(self):
        self._mmu = MemoryManagementUnit()

    def run_process(self, process: Process, memory: Memory):
        # tentar page-in #
        if (memory.has_space_for(process.pagina)):
            # page
            pass
        else:
            memory.disk_alloc(process)
            # adicionar

        # print process line
        print('|-|'*process.tempo_espera)

        count = process.tempo_restante
        while (count):
            for _ in range(0, process.tempo_execucao):
                print(f'|{process.char}|')
                count -= 1
                sleep()

        print('\n')
