# Simulador de execução de processos de um sistema operacional

### Algoritmos de escalonamento implementados:
  - FIFO
  - SJF
  - Round Robim
  - EDF

### O usuário deve digitar o nome do algoritmo de escalonamento e os dados do processo e do sistema
  - Existe um comando make para cada algoritmo passando o arquivo com entrada válidas para cada algoritmo.
  #Exemplo de Entrada: 
  ```
  edf
  3 2 1
  a 0 4 1
  b 2 3 2
  c 0 4 2
  ```
  
  - Onde o algoritmo escolhido foi o edf
  - 3 é o numero de processos
  - 2 é o quantun 
  - 1 é a sobrecarga do sistema
  - a é o caracter que representa o processo no gráfico de gant
  - o primeiro número representa o tempo de chegada
  - o segundo número representa o tempo de execução
  - o terceiro número representa a deadline do processo
  - para o FIFO e o SJF o terceiro número representa a deadline do processo
  
  #### Para os algoritmos de Fifo e SJF deve ser informado a quantidade de páginas e não deve ser informado valor de sobrecarga e valores de prioridade/deadline
  - O algoritmo de Round Robim foi implementado com e sem prioridade.
  - Para executar com prioridade deve ser executado com o comando "make prioridade"
  - Para executar sem prioridade deve ser executado com o comando "make rr"
  - O algoritmo de troca de páginas de Fifo foi implementado para os algoritmos de escalonamento Fifo e SJF
 
#### O gráfico de gant é exibido no terminal com a execução de cada processo
  
```  
Equipe:
Daniele Valverde
Valdinei Oliveira
```
