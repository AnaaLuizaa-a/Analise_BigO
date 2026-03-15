def imprimir_pares_e_soma(lista);
    for i in range (len(lista)):
        print (lista[i])
    for i in range (len(lista)):
        for j in range (i+1, len(lista)):
            print (lista[i], lista[j])
"""
A logica foi que esse algoritmo é O(n^2) porque tem um loop dentro do outro, ou seja, para cada elemento da lista, ele percorre a lista novamente para encontrar os pares. 
Portanto, o número de operações cresce quadráticamente com o tamanho da lista.
"""
