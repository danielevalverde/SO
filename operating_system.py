from dataclasses import dataclass
from processor import Processor


@dataclass
class OperatingSystem:
    delay: int
    processor: Processor

    def run(self):
        # recebe os dados de entrada
        # ordena os processos
        # escolhe o algoritmo de escalonamento com um switch
        # o algoritmo escolhido chama o execute_program, que roda por u.t. e ir decrementando no objeto do processo

        pass
