# Exercícios de Análise de Complexidade Assintótica (Big-O)

**Disciplina:** Estruturas de Dados e Análise de Algoritmos  
**Professor:** Alexandre de Oliveira  
**Aluna:** Ana Luiza Mattos de Carvalho  
**RA:** 124114111

---

## Exercício 1
```python
def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]
```
Complexidade: O(1)  
Justificativa: São realizadas operações de tempo constante, como verificar tamanho da lista e aceessar elemento por índice

---

## Exercício 2
```python
def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
```
Complexidade: O(n)  
Justificativa: O algoritmo possui laço de repetição que percorre cada um dos n elementos da lista uma única vez para realizar a soma.

---

## Exercício 3

```
def busca_binaria(lista, alvo):
esquerda, direita = 0 , len(lista) - 1
while esquerda <= direita:
meio = (esquerda + direita) // 2
if lista[meio] == alvo:
return meio
elif lista[meio] < alvo:
esquerda = meio + 1
else:
direita = meio - 1
return -
```
**Sua análise:**
Complexidade: O(n)  
Justificativa: A logica foi que esse algoritmo é logarítmico (O(log n)) pois ele divide a lista em duas partes a cada iteração.
Então ele espera o loop percorrer apenas os elementos necessários antes de devolver o resultado

---

## Exercício 4

```
def pares_com_soma(lista, alvo):
for i in range(len(lista)):
for j in range(i + 1 , len(lista)):
if lista[i] + lista[j] == alvo:
print(lista[i], lista[j])
```
**Sua análise:**
Complexidade: O(n^2) 
Justificativa: Onde o primeiro loop percorre a lista e o segundo loop percorre a lista a partir do próximo elemento do primeiro loop. 
Isso significa que para cada elemento da lista, o segundo loop percorre o restante da lista, resultando em um número de operações proporcional ao quadrado do tamanho da lista. 

---

## Exercício 5

```
def imprimir_pares_e_soma(lista):
# Bloco 1: imprime cada elemento
for i in range(len(lista)):
```

```
print(lista[i])
```
```
# Bloco 2: imprime todos os pares
for i in range(len(lista)):
for j in range(len(lista)):
print(lista[i], lista[j])
```
**Sua análise:**
Complexidade: O(n^2)  
Justificativa: A logica foi que esse algoritmo é O(n^2) porque tem um loop dentro do outro, ou seja, para cada elemento da lista, ele percorre a lista novamente para encontrar os pares. 
Portanto, o número de operações cresce quadráticamente com o tamanho da lista.

---

## Exercício 6

```
def potencias_de_dois(n):
i = 1
while i < n:
print(i)
i *= 2
```
**Sua análise:**
Complexidade: O(log n)  
Justificativa: A logica foi que esse algoritmo é O(log n) porque a cada iteração o valor de i é multiplicado por 2, ou seja, o número de iterações necessárias para alcançar ou ultrapassar n é proporcional ao logaritmo de n na base 2.
Portanto, o tempo de execução do algoritmo cresce de forma logarítmica em relação ao tamanho da entrada n.

---

## Exercício 7

```
def fibonacci_recursivo(n):
if n <= 1 :
return n
return fibonacci_recursivo(n - 1 ) + fibonacci_recursivo(n - 2 )
```
**Sua análise:**
Complexidade: O(2^n)  
Justificativa: A logica foi que esse algoritmo é O(2^n) porque a cada chamada recursiva ele faz duas chamadas para n-1 e n-2, ou seja, o número de chamadas é proporcional a 2 elevado a n.
Portanto, o tempo de execução do algoritmo cresce de forma exponencial em relação ao tamanho da entrada n.

---

## Exercício 8

```
def ordenacao_bolha(lista):
n = len(lista)
for i in range(n):
for j in range( 0 , n - i - 1 ):
if lista[j] > lista[j + 1 ]:
```

```
lista[j], lista[j + 1 ] = lista[j + 1 ], lista[j]
return lista
```
**Sua análise:**
Complexidade: O(2^n)   
Justificativa: A logica foi que esse algoritmo é O(2^n) porque ele tem um loop dentro de outro.

---

## Exercício 9

```
def produto_de_matrizes(A, B, n):
C = [[ 0 ] * n for _ in range(n)]
for i in range(n):
for j in range(n):
for k in range(n):
C[i][j] += A[i][k] * B[k][j]
return C
```
**Sua análise:**
Complexidade: O(n^3)  
Justificativa: A logica foi que esse algoritmo é O(n^3) porque ele tem três loops aninhados.

---

## Exercício 10

```
def merge_sort(lista):
if len(lista) <= 1 :
return lista
```
```
meio = len(lista) // 2
esquerda = merge_sort(lista[:meio])
direita = merge_sort(lista[meio:])
```
```
resultado = []
i = j = 0
while i < len(esquerda) and j < len(direita):
if esquerda[i] <= direita[j]:
resultado.append(esquerda[i])
i += 1
else:
resultado.append(direita[j])
j += 1
```
```
resultado.extend(esquerda[i:])
resultado.extend(direita[j:])
return resultado
```
**Sua análise:**
Complexidade: O(n log n)  
Justificativa: A logica foi que esse algoritmo é O(n log n) porque ele divide a lista em duas partes iguais a cada passo (log n) e depois combina as partes (n). O merge sort é eficiente para grandes conjuntos de dados e é estável, o que significa que mantém a ordem relativa dos elementos iguais.

---

## Tabela com as complexidades Big-O


|Complexidade | Descrição | Exemplo de Algoritmo|
| :---: | :---: | :---: |
|O(1) | Tempo constante | Acesso a um elemento em um array|
|O(log n) | Tempo logarítmico | Busca binária|
|O(n) | Tempo linear | Percorrer um array|
|O(n log n) | Tempo linearítmico | Merge Sort|
|O(n²) | Tempo quadrático | Bubble Sort|
|O(2ⁿ) | Tempo exponencial | Fibonacci recursivo|
|O(n!) | Tempo fatorial | Permutaçãos de um conjunto|


