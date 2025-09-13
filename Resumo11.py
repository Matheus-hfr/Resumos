#Tipos de exceções

try:                                           #Bloco que pode gerar um erro         
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
    print(f"O resultado é: {r}")
except (ValueError, TypeError):         #VALUE: VALOR INVÁLIDO EX: int("abc") / TYPE: TIPO ERRADO EX: len(123)
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:               #Erro ao tentar dividir por zero
    print("Não é possível dividir por zero.")

#Tipos específicos de exceções
lista = [1, 2, 3]
try:
    print(lista[6])                     #IndexError: índice fora do intervalo da lista
except IndexError:
    print("Erro ao acessar um índice inválido da lista.")
except TypeError:
    print("Tipo de dado incorreto.")

try:
    x= 10 / 0
except Exception as e:          #Captura qualquer tipo de exceção
    print(f"Ocorreu um erro: {e}")

#Finally
try:                                          #Bloco que pode gerar um erro
    print("Calculadora de divisão")
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
    print(f"O resultado é: {r}")
except Exception as e:                         #Captura qualquer tipo de exceção
    print(f"Ocorreu um erro: {e}")
finally:                                       #Bloco que sempre será executado
    print("Volte sempre! Muito obrigado!")
