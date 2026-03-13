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
Complexidade: O( __ )  
Justificativa: _______________________________________________

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
Complexidade: O( __ )  
Justificativa: _______________________________________________

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
Complexidade: O( __ )  
Justificativa: _______________________________________________

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
Complexidade: O( __ )  
Justificativa: _______________________________________________

---

## Exercício 7

```
def fibonacci_recursivo(n):
if n <= 1 :
return n
return fibonacci_recursivo(n - 1 ) + fibonacci_recursivo(n - 2 )
```
**Sua análise:**
Complexidade: O( __ )  
Justificativa: _______________________________________________

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
Complexidade: O( __ )  
Justificativa: _______________________________________________

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
Complexidade: O( __ )  
Justificativa: _______________________________________________

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
Complexidade: O( __ )  
Justificativa: _______________________________________________

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


