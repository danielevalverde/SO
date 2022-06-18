from process import Process
from processor import Processor


def sjf(plist: list[Process], processor: Processor):
    n = len(plist)
    checked = [False]*n
    clock = 0
    tot = 0
    items = []
    media_tempo_espera = 0
    media_turnaround = 0

    while (tot < n):
        min = max(p.tempo_execucao for p in plist)+1
        c = None

        for i in range(0, n):
            # If i'th process arrival time <= system time and its flag=0 and burst<min
            # That process will be executed first
            if ((plist[i].tempo_chegada <= clock) and (not checked[i]) and (plist[i].tempo_execucao < min)):
                min = plist[i].tempo_execucao
                c = i

        # If c==n means c value can not updated because no process arrival time< system time so we increase the system time */
        if (c == None):
            clock += 1
        else:
            items.append(plist[c])

            # ct[c] = clock+plist[c].tempo_execucao
            plist[c].turnaround = (
                clock+plist[c].tempo_execucao)-plist[c].tempo_chegada
            plist[c].tempo_espera = clock

            clock += plist[c].tempo_execucao
            checked[c] = True
            tot += 1

    for i in range(0, n):
        items[i].tempo_restante = items[i].tempo_execucao

        processor.run_process(items[i])

        media_tempo_espera += items[i].tempo_espera
        media_turnaround += items[i].turnaround

    media_tempo_espera /= n
    media_turnaround /= n

    return items
