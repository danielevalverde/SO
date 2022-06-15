import abc
from dataclasses import dataclass, field


class IMemoryManagementUnit(metaclass=abc.ABCMeta):
    address_mapping_table = {}

    @abc.abstractmethod
    def get_physical_address(self, virtual_address: str):
        """Pega o endereço virtual e retorna o físico """
        pass


@dataclass
class Process():
    arrival_time: int
    burst_time: int
    deadline: int
    waiting_time: int
    turn_around: int


@dataclass
class IProcessor(metaclass=abc.ABCMeta):
    _mmu: IMemoryManagementUnit = field(init=False)

    @abc.abstractmethod
    def execute_process(process: Process):
        """Execute the process"""
        pass


@dataclass
class IOperatingSystem(metaclass=abc.ABCMeta):
    overload: int
    quantum: int
    delay: int

    @abc.abstractmethod
    def run():
        # recebe os dados de entrada
        # ordena os processos
        # escolhe o algoritmo de escalonamento com um switch
        # o algoritmo escolhido chama o execute_program, que roda por u.t. e ir decrementando no objeto do processo
        pass

    @abc.abstractmethod
    def execute_program():
        # Executa todo ciclo de vida de um programa aqui
        # TODO: o que fazer com as páginas na memória quando ocorre sobrecarga do Round-Robin?
        # TODO: se os processos são executados um por vez, pelos algoritmos de escalonamento, como a paginação seria um problema?
        pass
