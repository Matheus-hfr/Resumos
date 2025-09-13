import re

#Validar email
email = "teste@gmail.com"
padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print(bool(re.match(padrao, email)))  # True

#Extrair números de telefone
texto = "Me ligue: 1234-5678 ou 99999-1234"
print(re.findall(r"\d{4,5}-\d{4}", texto))
# ['1234-5678', '99999-1234']

#Substituir números
frase = "O preço é 150 reais"
print(re.sub(r"\d+", "X", frase))
# O preço é X reais

#Extrair números de um texto
texto = "Idades: Ana 23, João 35, Maria 19"
print(re.findall(r"\d+", texto))
# ['23', '35', '19']