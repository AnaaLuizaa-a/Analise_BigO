def produto_de_matrizes(A,B,n):
    C = [[0] * n for _ in range (n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
"""
A logica foi que esse algoritmo é O(n^3) porque ele tem três loops aninhados.
"""
