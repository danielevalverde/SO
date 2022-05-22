from process import Process
import fifo

n = int(input())

list = []

for i in range(n):
  aux = Process()
  aux.tc, aux.te = input().split()
  list.append(aux)

# algorithm = input()

# for obj in list:
#   print(obj.x)

# for i in range(0, n ):
#   print(list[i].x)

print('\n')

fifo.run(n, list)