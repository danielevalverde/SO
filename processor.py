from dataclasses import dataclass, field
from time import sleep
from memory import Memory

from mmu import MemoryManagementUnit
from process import Process


@dataclass
class Processor:
    delay: int = field(default=0)
    _mmu: MemoryManagementUnit = field(
        default=MemoryManagementUnit(), init=False)
    # overload: int

    def run_process(self, process: Process):
        # # tentar page-in #
        # if (memory.has_space_for(process.pagina)):
        #     # page
        #     pass
        # else:
        #     memory.disk_alloc(process)
        #     # adicionar

        # print process line
        print('|-|'*process.tempo_espera, end='')

        count = process.tempo_restante
        while (count):
            # for _ in range(0, process.tempo_execucao):
            sleep(self.delay)
            print(f'|{process.char}|', end='', flush=True)
            count -= 1

        print('')
