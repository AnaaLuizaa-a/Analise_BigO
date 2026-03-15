def pares_com_soma(lista,alvo):
    for i in range (len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == alvo:
                print(lista[i], lista[j])
"""
A logica foi que esse algoritmo é O(n^2) porque ele tem dois loops aninhados.
Onde o primeiro loop percorre a lista e o segundo loop percorre a lista a partir do próximo elemento do primeiro loop. 
Isso significa que para cada elemento da lista, o segundo loop percorre o restante da lista, resultando em um número de operações proporcional ao quadrado do tamanho da lista. 
"""
