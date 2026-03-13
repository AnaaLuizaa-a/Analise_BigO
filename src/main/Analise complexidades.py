def somar_lista(lista):
    total = 0
    for elemento in lista: #O(n)
        total += elemento
    return total
"""
A logica foi que esse algoritmo é linear (O(n)) pois o return está fora do bloco for. 
Então ele espera o loop percorrer todos os n elementos antes de devolver o resultado
"""
