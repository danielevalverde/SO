from dataclasses import dataclass, field
from time import sleep
from memory import Memory

from mmu import MemoryManagementUnit
from process import Process


@dataclass
class Processor:
    algorithm: str
    overload: int
    quantum: int
    processes: list[Process]
    _mmu: MemoryManagementUnit = field(init=False)

    def run_process(self, process: Process, memory: Memory):
        # tentar page-in #
        if (memory.has_space_for(process.pg)):
            # page
            pass
        else:
            memory.disk_alloc(process)
            # adicionar

        # print process line
        print('|-|'*process.wt)

        while (process.trf):
            for _ in range(0, process.te):
                print(f'|{process.char}|')
                process.trf -= 1
                sleep()

        print('\n')
