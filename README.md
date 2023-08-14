# nomeclaturaComDFS
Aplicação do busca em profundidade (ou busca em profundidade-primeiro, também conhecido em inglês por Depth-First Search - DFS) para nomenclatura de arestas.

DEFINIÇÃO DAS ARESTAS
● Aresta de Árvore: A aresta (u, v) é uma aresta de árvore se v foi descoberto pela primeira vez ao percorrer a aresta (u, v);
● Aresta de Retorno: Conecta um vértice u com o antecessor v na árvore de busca. Ex: aresta tipo laço;
● Aresta de Avanço: Conecta um vértice a um descendente que pertence a árvore de busca;
● Aresta de Cruzamento: Conecta um vértice u a um vértice v que já teve todos os seus vizinhos explorados.

ENTRADA.TXT
● Na linha 1 do arquivo, se encontra nesta ordem, o número de vértices, o número de arestas e se o grafo é direcionado (D) ou não direcionado (N);
● Se na linha 1 do arquivo, for informado que o grafo possui X arestas, então o arquivo deve conter X + 1 linhas, sendo a linha 1 contendo informações sobre o grafo em geral e as linhas restantes, as arestas entre os vértices do grafo;
● Cada linha do arquivo (com exceção da linha 1) contém um vértice u, seguido de um vértice v. Se o grafo for direcionado (D), indica que o vértice u "aponta" para o vértive v, o contrário não acontece (há não ser que haja uma linha no formato (v, u)). Se o grfo for não direcionado (N), indica que há uma aresta entre os dois vértices.
