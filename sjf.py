def sjf(dict):
    begHold, endHold = 0, 0
    sjfdict, tempdict, sortdict, pLine = {}, {}, {}, []

    for key, value in dict.items():
        tempo_chegada, tempo_execucao = value[0], value[1]
        if (begHold == 0):
            endHold += tempo_execucao
            sjfdict[key] = [begHold-tempo_chegada,
                            tempo_execucao-tempo_chegada]
            pLine.append([key, endHold])
            begHold = tempo_execucao
        else:
            tempdict[key] = value[0], value[1]

    for key, value in sorted(tempdict.items(), key=lambda x: x[1][1]):
        sortdict[key] = value[0], value[1]

    for key, value in sortdict.items():
        tempo_chegada, tempo_execucao = value[0], value[1]
        if(begHold-tempo_chegada > 0):
            endHold += tempo_execucao
            sjfdict[key] = [begHold-tempo_chegada, endHold-tempo_chegada]
            pLine.append([key, endHold])
            begHold += tempo_execucao
        else:
            endHold += tempo_execucao
            sjfdict[key] = [0, tempo_execucao]
            pLine.append([key, endHold+1])
            begHold += tempo_execucao

    return sjfdict, pLine
