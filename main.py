# import fifo as fifo

from process import Process

n = int(input())

list = []

for i in range(n):
  aux = Process()
  aux.x, aux.y = input().split()
  list.append(aux)

algorithm = input()

for obj in list:
  print(obj.x)