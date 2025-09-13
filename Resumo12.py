try:
    arquivo = open('arquivo.txt', 'w', encoding='utf-8') #open abre o arquivo, 'w' é para escrita, encoding define a codificação de caracteres
    arquivo.write('Ola Mundo!') #Escreve no arquivo
    arquivo.write('Este é um arquivo de exemplo em python.')
    print('Dados escritos com sucesso no arquivo.')
except Exception as e:
    print(f'Ocorreu um erro ao manipular o arquivo: {e}')
finally:
    if 'arquivo' in locals(): #Verifica se o arquivo foi aberto
        arquivo.close() #Fecha o arquivo
        print('Arquivo fechado.')

#Lendo um arquivo
try:
    arquivo = open('arquivo.txt', 'r', encoding='utf-8') #Abre o arquivo em modo de leitura
    conteudo = arquivo.read() #Lê o conteúdo do arquivo
    print(conteudo)
except FileNotFoundError:
    print('Arquivo não encontrado.')
except Exception as e:
    print(f'Ocorreu um erro ao ler o arquivo: {e}') 
finally:
    if 'arquivo' in locals() and not arquivo.closed: #Verifica se o arquivo foi aberto e não está fechado
        arquivo.close()
        print('Arquivo fechado.') 

#Usando with para manipulação de arquivos
try:
    with open('arquivo.txt', 'r', encoding='utf-8') as arquivo: #Abre o arquivo e garante que será fechado automaticamente
        conteudo = arquivo.read()
        print(conteudo)
except Exception as e:
    print(f'Ocorreu um erro ao ler o arquivo: {e}')
#Não é necessário fechar o arquivo, o with faz isso automaticamente

#OS - Operações com o sistema operacional
import os

caminho_atual = os.getcwd() #Obtém o diretório atual
print(f'Diretório atual: {caminho_atual}')

#Listar arquivos e diretórios
print('Conteúdo do diretório atual:')
for item in os.listdir(caminho_atual):
    print(f" - {item}")

#Criar um novo diretório
nome_novo_diretorio = 'novo_diretorio_os'
if not os.path.exists(nome_novo_diretorio): #Verifica se o diretório já existe
    os.mkdir(nome_novo_diretorio)
    print(f'Diretório "{nome_novo_diretorio}" criado com sucesso.')
else:
    print(f'Diretório "{nome_novo_diretorio}" já existe.')

#Remover um diretório
try:
    os.rmdir(nome_novo_diretorio) #Remove o diretório (deve estar vazio)
    print(f'Diretório "{nome_novo_diretorio}" removido com sucesso.')
except FileNotFoundError:
    print(f'Diretório "{nome_novo_diretorio}" não encontrado.')
except OSError:
    print(f'Diretório "{nome_novo_diretorio}" não está vazio.')