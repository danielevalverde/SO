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

    def fifo(self):
        list_size = len(self.processes)
        wt = 0
        ta = 0
        for i in range(0, list_size):
            self.processes[i].wt = int(wt)
            self.processes[i].ta = int(self.processes[i].te) + ta
            wt = int(self.processes[i].te) + int(wt)
            ta = ta + int(self.processes[i].te)

        wt = wt - int(self.processes[list_size-1].te)
        # print('---------------------------')

        print("Processes Burst time " +
              " Waiting time " +
              " Turn around time")

        for i in range(0, list_size):
            print(" " + str(i + 1) + "\t\t" +
                  str(self.processes[i].te) + "\t " +
                  str(self.processes[i].wt) + "\t\t " +
                  str(self.processes[i].ta) + "\t\t ")

        print("Average waiting time = " + str(wt / list_size))
        print("Average turn around time = " + str(ta / list_size))

        return

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
