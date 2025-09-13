#Condicionais

idade = 18
if idade < 18:
    print("Menor de idade") # Se a idade for menor que 18
elif idade == 18:
    print("Tem 18 anos") # Se a idade for exatamente 18
else:
    print("Maior de idade") # Se a idade for maior que 18

#Operador ternário
idade = 20

status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
