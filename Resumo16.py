#API's

import requests
import json

#GET
url_joke_api = "https://v2.jokeapi.dev/joke/Any"

try:
    print(f"Fazendo requisição GET para: {url_joke_api}")
    response = requests.get(url_joke_api) #Fazendo a requisição GET

    #Verifica se a requisição foi bem-sucedida
    print(f"Status Code: {response.status_code}")
    #Exceção para status code diferente de 200
    response.raise_for_status()
    dados = response.json() #Converte a resposta JSON em um dicionário Python
    print(json.dumps(dados, indent=4, ensure_ascii=False)) #Imprime o dicionário formatado

    if dados.get("error") == False:
        print(f"\nPiada: {dados.get('joke')}")
        print(f"Categoria: {dados.get('category')}")
    else:
        print("Erro ao obter a piada.")

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


#POST
url_posts_api = "https://jsonplaceholder.typicode.com/posts"
novo_post_dados = {
    "title": "Meu Novo Post",
    "body": "Este é o conteúdo do meu novo post usando a biblioteca requests!",
    "userId": 101
}
try:
    print(f"\nFazendo requisição POST para: {url_posts_api}")
    response = requests.post(url_posts_api, json=novo_post_dados) #Fazendo a requisição POST

    #Verifica se a requisição foi bem-sucedida
    print(f"Status Code: {response.status_code}")
    #Exceção para status code diferente de 201 (Created)
    response.raise_for_status()
    dados_post = response.json() #Converte a resposta JSON em um dicionário Python
    print(json.dumps(dados_post, indent=4)) #Imprime o dicionário formatado
    print(f"\nPost criado com ID: {dados_post.get('id')}")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}") 
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")  
