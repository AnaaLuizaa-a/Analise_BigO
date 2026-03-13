def verificar_primeiro(lista):
    if len(lista) == 0: #O(1)
        return None
    return lista[0]
"""
A logica foi que esse algoritmo é constante (O(1)), pois vai consultar um atributo interno que ja tem o numero armazenado em len(lista)
e acessou um indice especifico (com lista[0]) diretamente. 
Como o código executou o mesmo numero de passos fixos independente da entrada, ele é de complexidade constante
"""
