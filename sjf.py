from process import Process


def sjf(list: list[Process]):
    acc_inicio, acc_execucao = 0, 0
    sjfdict, tempdict, sortdict = {}, {}, {}, []

    for key, process in enumerate(list):
        tempo_chegada, tempo_execucao = process.tc, process.te
        if (acc_inicio == 0):
            acc_execucao += tempo_execucao
            sjfdict[process.char] = process
            acc_inicio = tempo_execucao
        else:
            tempdict[process.char] = process

    for key, process in sorted(tempdict.items(), key=lambda x: x[1][1]):
        sortdict[key] = process.tc, process.te

    for key, process in sortdict.items():
        tempo_chegada, tempo_execucao = process.tc, process.te
        if(acc_inicio-tempo_chegada > 0):
            acc_execucao += tempo_execucao
            sjfdict[key] = [acc_inicio-tempo_chegada,
                            acc_execucao-tempo_chegada]
            acc_inicio += tempo_execucao
        else:
            acc_execucao += tempo_execucao
            sjfdict[key] = [0, tempo_execucao]
            acc_inicio += tempo_execucao

    return sjfdict.values()
