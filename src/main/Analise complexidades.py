def ordenacao_bolha(lista):
    n = len(lista)
    for i in range (n):
        for j in range (0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
"""
A logica foi que esse algoritmo é O(2^n) porque ele tem um loop dentro de outro.
"""
