import json 

#Dados Python
dados = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

#Convertendo para JSON
json_string = json.dumps(dados)
print('String JSON(sem formatação):')
print(json_string)

#Convertendo para JSON com indentação
json_string_formatada = json.dumps(dados, indent=4,sort_keys=True)
print('\nString JSON(com formatação):')
print(json_string_formatada)

#Serializando para um arquivo JSON
nome_arquivo_json = 'dados_matheus.json'
try:
    with open(nome_arquivo_json, 'w', encoding='utf-8') as f_json:
        json.dump(dados, f_json, indent=4, sort_keys=True) #Serializa e escreve no arquivo
    print(f'Dados serializados e salvos em {nome_arquivo_json}')
except Exception as e:
    print(f'Erro ao escrever no arquivo: {e}')

#Desserializando de um arquivo JSON
try:
    with open(nome_arquivo_json, 'r', encoding='utf-8') as f_json:
        dados_carregados = json.load(f_json) #Desserializa o conteúdo do arquivo
    print('\nDados carregados do arquivo JSON:')
    print(dados_carregados)
except FileNotFoundError:
    print(f'Arquivo {nome_arquivo_json} não encontrado.')
except Exception as e:
    print(f'Erro ao ler o arquivo: {e}')