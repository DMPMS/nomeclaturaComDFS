def organizarLista(lista: list) -> None:
    """
    Recebe uma lista de listas e organiza a lista colocando todos os elementos
    iguais ao elemento da lista[i][0] no início da lista[i]. Em seguida, ordena
    os elementos restantes e os coloca no fim da lista.
    """
    for i in range(len(lista)):
        vertice = lista[i][0]
        cont = 1
        for j in range(1, len(lista[i])):
            if lista[i][j] == vertice:
                cont += 1
        for k in lista[i].copy():
            if k == vertice:
                lista[i].remove(k)
        lista[i].sort()
        for l in range(cont):
            lista[i].insert(0, vertice)
    lista.sort()

def imprimirLista(lista: list) -> None:
    """
    Recebe uma lista de listas e imprime ela no formato da representação de uma
    lista de adjacência.
    """
    for i in range(len(lista)):
        for k in range(len(lista[i])):
            print(f"{lista[i][k]} -> ", end="")
        print()

def carregarArquivo(arquivo: str) -> None:
    """
    Recebe uma string contendo o caminho do diretório de um arquivo e
    retorna a matriz de adjacência gerada apartir do conteúdo deste
    arquivo.
    """
    arquivoAberto = open(arquivo, 'r')
    listaDaEntrada = arquivoAberto.readlines()

    # Lista que representará nosa lista de adjacência.
    listaDaSaida = []

    for i in range(len(listaDaEntrada)):
        linha = listaDaEntrada[i].split()
        # Caso seja a primeira linha do arquivo, defino se é um grafo direcionado ou não.
        if i == 0:
            if linha[2] == "D":
                direcionado = True
            elif linha[2] == "N":
                direcionado = False
        # Caso não seja a primeira linha do arquivo, começo a preencher a lista de saída.
        else:
            # Verifico se a lista do vértice linha[0] já está na lista de saída. Caso esteja, defino qual o índice dessa lista na lista de saída.
            estaNaLista = False
            for i in range(len(listaDaSaida)):
                if listaDaSaida[i][0] == linha[0]:
                    estaNaLista = True
                    indiceDaListaDoVerticeLinha0 = i
            # Caso a lista do vértice linha[0] não esteja na lista de saída, é criado essa lista com o vértice linha[0] dentro dela e definimos
            # qual o indice da lista do vértice linha[0].
            if not estaNaLista:
                listaDaSaida.append([linha[0]])
                indiceDaListaDoVerticeLinha0 = listaDaSaida.index([linha[0]])
            # Caso seja um grafo direcionado, adiciono à lista do vértice linha[0] o vértice linha[1], indicando que há a aresta de linha[0] para linha[1].  
            if direcionado:             
                listaDaSaida[indiceDaListaDoVerticeLinha0].append(linha[1])
            # Caso seja um grafo não direcionado, adiciono à lista do vértice linha[0] o vértice linha[1] e adiciono à lista do vértice linha[1] o vértice linha[0],
            # indicanto que há a aresta entre estes vértices.
            elif not direcionado:
                # Adicionando à lista do vértice linha[0] o vértice linha[1].

                # Caso seja um laço só adiciono uma vez.
                if linha[0] == linha[1]:
                    listaDaSaida[indiceDaListaDoVerticeLinha0].append(linha[1])
                else:
                    listaDaSaida[indiceDaListaDoVerticeLinha0].append(linha[1])

                    # Verifico se a lista do vértice linha[1] já está na lista de saída. Caso esteja, defino qual o índice dessa lista na lista de saída.
                    estaNaLista = False
                    for i in range(len(listaDaSaida)):
                        if listaDaSaida[i][0] == linha[1]:
                            estaNaLista = True
                            indiceDaListaDoVerticeLinha1 = i
                    
                    # Caso a lista do vértice linha[1] esteja na lista de saída, adiciono o vértice linha[0] à lista.
                    if estaNaLista:
                        listaDaSaida[indiceDaListaDoVerticeLinha1].append(linha[0])
                    # Caso a lista do vértice linha[1] não esteja na lista de saída, adiciono à lista de saída a lista do vértice linha[1], defino qual o 
                    # índice da lista do vértice linha[1] e adiciono a esta lista o vértice linha[1] e o vértice linha[0], respectivamente.
                    elif not estaNaLista:
                        listaDaSaida.append([linha[1]])
                        indiceDaListaDoVerticeLinha1 = listaDaSaida.index([linha[1]])
                        listaDaSaida[indiceDaListaDoVerticeLinha1].append(linha[0])

    arquivoAberto.close()
    organizarLista(listaDaSaida)    
    imprimirLista(listaDaSaida)

if __name__ == '__main__':
    carregarArquivo("entrada.txt")