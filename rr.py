from operator import iadd
from time import sleep
from process import Process

list_of_process = []


def run(n, list):
    wt = 0
    ta = 0
    i = 0
    while(i < n):
        list[i].wt = int(wt)
        if(int(list[i].trf) > 0):
            if(int(list[i].trf) >= int(list[i].qa)):
                # se o tempo de exec restate > quantun
                wt = int(list[i].qa) + int(wt)
                list[i].trf = int(list[i].trf) - int(list[i].qa)
                list[i].ta = int(list[i].qa) + ta 
                ta = ta + int(list[i].qa)
                # se depois de executar até o tempo do quantun, o processo ainda precisar de mais tempo pra executar, colocamos ele novamente na lista
                if(int(list[i].trf) >0): 
                  aux = Process()
                  aux.wt = list[i].wt
                  aux.te = list[i].te
                  aux.trf = list[i].trf
                  aux.qa = list[i].qa
                  list.append(aux)
                  n += 1
                print('   ' * list[i].wt,end='')
                for j in range(0, list[i].qa):
                  sleep(1)
                  print('|'+list[i].char + '|',end='', flush=True)
                print('\n')
            else:
                wt = int(list[i].trf) + int (wt)
                ta = ta + int(list[i].trf)
                list[i].ta =  ta
                print('   ' * list[i].wt,end='')
                for j in range(0, list[i].trf):
                  sleep(1)
                  print('|'+list[i].char + '|', flush=True)
                print('\n')
                list[i].trf = 0
        i += 1
    print('\n')
    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")

    for i in range(0, n):
        print(" " + str(i + 1) + "\t\t" +
              str(list[i].te) + "\t " +
              str(list[i].wt) + "\t\t " +
              str(list[i].ta) + "\t\t ")

    print("Average waiting time = " + str(wt / n))
    print("Average turn around time = " + str(ta / n))

    # print(wt)
    # print(ta)
