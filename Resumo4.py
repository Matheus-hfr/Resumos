#Laços de repetição

# for            usado para iterar sobre uma sequência (como listas, tuplas, strings) ou um intervalo de números

#Lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")  # Passa/repete sobre cada fruta na lista

#String
palavra = "Python"
for letra in palavra:
    print(letra)  # Passa/repete sobre cada letra na string

#Range
for i in range(5):
    print(i)  # Passa sobre números de 0 a 4           contagem começa do 0 e vai até n-1

for i in range(2, 6):
    print(i)  # Passa sobre números de 2 a 5           contagem começa do 2 e vai até n-1

for i in range(1, 10, 2):
    print(i)  # Passa sobre números ímpares de 1 a 9    contagem começa do 1, vai até n-1, pulando de 2 em 2

#Dicionário
contatos = {"Alice": "1234-5678", "Bob": "9876-5432", "Charlie": "5555-3210"}
print ("\nChaves:")
for nome in contatos:
    print(nome)  # Passa/repete sobre as chaves do dicionário

for nome in contatos.keys(): # Modo explícito de fazer o mesmo que acima
    print(nome)

print ("\nValores:")
for numero in contatos.values():
    print(numero)

print ("\nChave e Valor:")
for nome, numero in contatos.items():
    print(f"{nome}: {numero}")

# while         usado para repetir um bloco de código enquanto uma condição for verdadeira
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa o contador para evitar loop infinito

print("Fim do loop")

# break         usado para sair de um loop antes que ele termine naturalmente
for i in range(10):
    if i == 5:
        print("5 encontrado, saindo do loop.")
        break  # Sai do loop quando i é igual a 5
    print(i)
print("Fim do loop")

# continue      usado para pular a iteração atual e continuar com a próxima iteração do loop
for i in range(10):
    if i % 2 == 0:
        continue  # Pula números pares
    print(i)  # Imprime apenas números ímpares

#Laços aninhados
for i in range(3):  # Loop externo
    print (f"Iteração externa {i}")
    for j in range(2):  # Loop interno
        print (f"  Iteração interna {j}")
    print("Fim da iteração externa")
print("Fim dos loops")
 