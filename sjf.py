class Processo:
    def __init__(self, tempo_chegada, tempo_execucao, deadline, quantum, sobrecarga):
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.deadline = deadline
        self.quantum = quantum
        self.sobrecarga = sobrecarga


def calc_tempo_espera(processos, num_processos):
    te_list = []

    te_list.append(0)

    for i in range(1, num_processos):
        te_list[i] = processos[i-1].tempo_execucao + te_list[i-1]

    return te_list


def calc_turn_around_time(processos, num_processos, espera_list):
    tat_list = []
    # calculating turnaround time by adding bt[i] + wt[i]
    for i in range(0, num_processos):
        tat_list.append(processos[i].bt + espera_list[i])

    return tat_list


def calc_tempo_medio(processos, num_processos):
    total_wt = 0
    total_tat = 0

    wt = calc_tempo_espera(processos, num_processos)

    tat = calc_turn_around_time(processos, num_processos)

    for i in range(0, num_processos):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    media_espera = float(total_wt) / float(num_processos)
    media_turn_around = float(total_tat) / float(num_processos)

    return {
        'media_espera': media_espera,
        'media_turn_around': media_turn_around
    }


def compare(processoA, processoB):
    return processoA.tempo_execucao < processoB.tempo_execucao

