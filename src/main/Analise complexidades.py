def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1
"""
A logica foi que esse algoritmo é logarítmico (O(log n)) pois ele divide a lista em duas partes a cada iteração.
Então ele espera o loop percorrer apenas os elementos necessários antes de devolver o resultado
"""
