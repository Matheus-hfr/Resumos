#Funções

def saudar():
    print("Olá, seja bem-vindo!")

#Chamando a função
saudar() #Saída: Olá, seja bem-vindo!    Pode ser chamada várias vezes

#Função com parâmetros
def saudar_usuario(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

saudar_usuario("Ana") #Saída: Olá, Ana! Seja bem-vindo!

#Função com multiplos parâmetros
def somar(a, b):
    resultado = a + b
    print(f"A soma de {a} e {b} é {resultado}")

#Parâmetros posicionais
def descrever_animal(tipo_animal,nome_animal):
    print(f"Eu tenho um {tipo_animal}.")
    print(f"O nome dele é {nome_animal}.")

descrever_animal("cachorro","Rex") #Recebe os argumentos na ordem correta!!!

#Parâmetros nomeados
def descrever_animal(tipo_animal,nome_animal):
    print(f"Eu tenho um {tipo_animal}.")
    print(f"O nome dele é {nome_animal}.")

descrever_animal(tipo_animal="cachorro", nome_animal="Rex") #Agora, os argumentos são passados pelo nome          A ordem não importa!
descrever_animal("gato", nome_animal="Mia") #Pode misturar os dois tipos, mas os posicionais devem vir primeiro

#Parâmetros padrão
def saudar_com_mensagem(nome, mensagem="Seja bem-vindo!"):
    print(f"Olá, {nome}. {mensagem}")

saudar_com_mensagem("Carlos") #Usa a mensagem padrão
saudar_com_mensagem("Maria", "Como você está?") #Usa a mensagem personalizada

#Retornando valores
def somar(a, b):
    soma = a + b
    return soma

resultado = somar(3, 5)
print(f"O resultado da soma é {resultado}") #Saída: O resultado da soma é 8

#Retornando múltiplos valores
def calcular(a, b):
    soma = a + b
    produto = a * b
    diferenca = a - b
    return soma, produto, diferenca

s, p, d = calcular(10, 5)
print(f"Soma: {s}, Produto: {p}, Diferença: {d}") #Saída: Soma: 15, Produto: 50, Diferença: 5

#Caso nao haja return, a função retorna None
def funcao_sem_retorno():
    x = 10

valor = funcao_sem_retorno()
print(resultado) #Saída: None

#Escopo de variáveis
x = 10  # Variável global

def minha_funcao():
    y= 5  # Variável local
    print(f"Valor dentro da função: {y}")   #Inacessível fora da função
    print(f"Valor da variável global dentro da função: {x}") #Acessível dentro e fora da função

minha_funcao()

#Modificando variáveis globais
contador = 0  # Variável global

def incrementar_contador():
    global contador  # Indica que queremos usar a variável global
    contador += 1
    print(f"Contador dentro da função: {contador}")

incrementar_contador()  # Saída: Contador dentro da função: 1
incrementar_contador()  # Saída: Contador dentro da função: 2
print(f"Contador fora da função: {contador}")  # Saída: Contador fora da função: 2

#Docstrings
def somar(a, b):            #Usado para documentar a função, explicando seu propósito, parâmetros e valor de retorno.
    """
    Retorna a soma de dois números.

    Parâmetros:
    a (int, float): O primeiro número.
    b (int, float): O segundo número.             

    Retorna:
    int, float: A soma de a e b.
    """
    return a + b