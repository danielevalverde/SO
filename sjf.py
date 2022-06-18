from process import Process


def sjf(plist: list[Process]):
    acc_inicio, acc_execucao = 0, 0
    sjfdict, tempdict, sortdict = {}, {}, {}

    for process in plist:
        if (acc_inicio == 0):
            acc_execucao += process.tempo_execucao
            sjfdict[process.char] = process
            acc_inicio = process.tempo_execucao
        else:
            tempdict[process.char] = process

    for key, process in sorted(tempdict.items(), key=lambda x: x[1].tempo_execucao):
        sortdict[key] = process

    for key, process in sortdict.items():
        acc_execucao += process.tempo_execucao

        if (acc_inicio-process.tempo_chegada > 0):
            process.tempo_espera = acc_inicio  # -process.tempo_chegada
            process.turnaround = acc_execucao-process.tempo_chegada
        else:
            process.tempo_espera = 0
            process.turnaround = process.tempo_execucao

        sjfdict[key] = process
        acc_inicio += process.tempo_execucao

    return list(sjfdict.values())
