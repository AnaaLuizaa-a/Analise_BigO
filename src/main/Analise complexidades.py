def potencias_de_dois(n):
    i = 1
    while i < n :
        print(i)
        i *= 2
"""
A logica foi que esse algoritmo é O(log n) porque a cada iteração o valor de i é multiplicado por 2, ou seja, o número de iterações necessárias para alcançar ou ultrapassar n é proporcional ao logaritmo de n na base 2.
Portanto, o tempo de execução do algoritmo cresce de forma logarítmica em relação ao tamanho da entrada n.
"""
