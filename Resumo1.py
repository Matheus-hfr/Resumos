#Variaveis

nome = 'Matheus' 
idade = 18
altura = 1.75
aprovado = True

#Imutabilidade
#As strings em Python são imutáveis, ou seja, não podem ser alteradas após a sua criação.
#Isso significa que, se você tentar modificar uma string, na verdade estará criando uma nova string.
nome_novo = "J" + nome[1:]

#Tipos de Dados

#Numeros Inteiros (INT)
quantidade = 10
estoque = -10

#Numeros Flutuantes (FLOAT)

preco = 19.90   
pi = 3.14159

#Numeros Complexos (COMPLEX)

z = 4 + 5j
print(f'Valor real : {z.real}') 
print(f'Valor imaginario : {z.imag}')

#Texto (STRING)
mensagem = "Olá, Mundo!"

#String Multilinha
mensagem_multilinha = """Olá,
Mundo!"""

print(mensagem)
print(mensagem_multilinha)

#Booleanos (BOOL)  #Apenas dois valores, usados para verificar condições
verdadeiro = True
falso = False

#Valor Nulo (NONE)
nulo = None

#Verificacao de dados
print(type(nome))              #type com parametro/argumento nome
print(type(idade))
print(type(altura))
print(type(aprovado))
print(type(quantidade))
print(type(estoque))
print(type(preco))
print(type(pi))
print(type(z))
print(type(mensagem))
print(type(mensagem_multilinha))
print(type(verdadeiro))
print(type(falso))
print(type(nulo))

#Conversao de tipos
idade_str = str(idade)  #int para str
altura_float = str(altura)  #float para str
tem_idade = bool(idade) #int para bool                   QUALQUER NUMERO INTEIRO É TRUE

#Concatenacao
mensagem_completa =" Você tem " + idade_str + " anos."
print(mensagem_completa)

#Formatacao de String
mensagem_formatada = f"Você tem {idade_str} anos."  
print(mensagem_formatada)

#Metodos Uteis

print(nome.upper())  #Deixa todas as letras maiusculas      #Metodos sempre sao chamados com parenteses mesmo sem argumentos
print(nome.lower())  #Deixa todas as letras minusculas
print(nome.title())  #Deixa a primeira letra de cada palavra maiuscula
print(nome.strip())  #Remove espacos em branco no inicio e no fim
print(nome.replace("Matheus", "João"))  #Substitui "Matheus" por "João" 
print(len(nome))  #Conta a quantidade de caracteres na string