#Listas 

lista_vazia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_strings = ["maçã", "banana", "laranja"]
lista_mista = [1, "dois", 3.0, True]
construtor_lista = list((7, 8, 9))  # Usando o construtor list()

#Acessando elementos    0 sempre será o primeiro elemento.
print(lista_numeros[0])  # Saída: 1
print(lista_strings[-1])  # Saída: laranja
print(lista_strings[-2])  # Saída: banana, retorna o penúltimo elemento

#Modificando elementos
lista_numeros[0] = 10 #Saída: [10, 2, 3, 4, 5]

#Fatiamento de listas
fatiamento = lista_numeros[1:4]  # Saída: [2, 3, 4]
fatiamento_inicio = lista_numeros[:3]  # Saída: [10, 2, 3]
fatiamento_fim = lista_numeros[2:]  # Saída: [3, 4, 5]

#Principais métodos de listas
lista_numeros.append(6)  # Adiciona 6 ao final da lista
lista_numeros.insert(0, 0)  # Insere 0 na posição 0
lista_numeros.remove(3)  # Remove o primeiro elemento com valor 3
removido = lista_numeros.pop(0)  # Remove e retorna primeiro elemento, Ex 0 foi removido
lista_numeros.sort()  # Ordena a lista em ordem crescente
lista_numeros.reverse()  # Inverte a ordem da lista
tamanho = len(lista_numeros)  # Retorna o tamanho da lista

#Listas aninhadas   
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[0]) # Saída: [1, 2, 3]
print(matriz[1][1]) # Saída: 5

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ') # Imprime todos os elementos da matriz adicionando um espaço entre eles
    print()  # Nova linha após cada linha da matriz
#Saída:
#1 2 3
#4 5 6
#7 8 9

#Tuplas
tupla_vazia = ()
coordenadas = (10, 20, 30, 40)
print(coordenadas[1])  # Saída: 20
#coordenadas[1] = 25  # Isso causará um erro, pois tuplas são imutáveis

#Conversão entre listas e tuplas
lista_para_tupla = tuple(lista_numeros)  # Converte lista para tupla
lista_temporaria = list(coordenadas)  # Converte tupla para lista
lista_temporaria.append(50)  # Modifica a lista temporária
nova_tupla = tuple(lista_temporaria)  # Converte de volta para tupla

#Métodos de tuplas
contagem = coordenadas.count(20)  # Conta quantas vezes 20 aparece na tupla
indice = coordenadas.index(30)  # Retorna o índice da primeira ocorrência de 30
print(contagem)  # Saída: 1
print(indice)  # Saída: 2