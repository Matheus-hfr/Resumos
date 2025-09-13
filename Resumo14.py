#Datetime

import datetime
from datetime import date

#Pega a data e hora atual
agora = datetime.datetime.now()
print("Data e hora atual:", agora)

#Pega apenas a data atual
hoje = date.today()
print("Data atual:", hoje)

# Criar uma data/hora específica
data = datetime(2025, 12, 25, 10, 30)
print(data)  # 2025-12-25 10:30:00

#datetime.strptime() → converter string → objeto datetime
data_str = "2025-12-25 10:30:00"
data_obj = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
print(data_obj)  # 2025-12-25 10:30:00

#datetime.strftime() → converter datetime → string formatada
data_formatada = data_obj.strftime("%d/%m/%Y %H:%M")
print(data_formatada)  # 25/12/2025 10:30