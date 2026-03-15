def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
"""
A logica foi que esse algoritmo é O(2^n) porque a cada chamada recursiva ele faz duas chamadas para n-1 e n-2, ou seja, o número de chamadas é proporcional a 2 elevado a n.
Portanto, o tempo de execução do algoritmo cresce de forma exponencial em relação ao tamanho da entrada n.
"""
