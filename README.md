# SO

- Round-Robin: adicionar sobrecarga e adicionar testes
- SJF: corrigir e testar
- MMU
  - Tabelas de endereços virtual e real
- Gerenciamento de Memória
  - Memória: vetor de 200K/4K = 50 posições para as páginas
  - Paginação: checar bit e espaço disponível, page-in, page-out
    - Remover LRU páginas e reorganizar (desfragmentar) memória
    - O algoritmo remove o conjunto de páginas de cada processo (como nas ilustrações)
    - TODO: Se por ex, no Round-Robin, um processo for pausado, as páginas dele podem ser substituídas se a memória ficar cheia?
  - PASSOS:
    - SE primeira execução:
      - Verifica espaço na memória. Se tiver, aloca as páginas. Senão, realiza substituição de páginas (de acordo com algoritmo).
        - Se substituiu todos possíveis e ainda não há espaço suficiente, manter em espera
          - TODO: adicionar campo para estado do processo
    - SE outra execução:
      - Atualiza timestamp do conjunto de páginas do processo
