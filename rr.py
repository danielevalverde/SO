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
                wt = int(list[i].qa) + int(wt)
                ta = ta + int(list[i].qa)
                list[i].trf = int(list[i].trf) - int(list[i].qa)
                list[i].ta = int(list[i].te) + ta
                list.push(list[i])
                n += 1
                for j in range(0, list[i].qa):
                    print('|'+list[j].char + '|')
            else:
                wt = int(list[i].trf) + int(wt)
                ta = ta + int(list[i].trf)
                list[i].ta = int(list[i].te) + ta
                for j in range(0, list[i].trf):
                    print('|'+list[j].char + '|')
                list[i].trf = 0
        i += 1
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
