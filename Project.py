import pandas as pd # importou a biblioteca para realizer leitura de arquivos CSV. Pandas é uma das bibliotecas
# mais utilizadas para ciencia de dados

df = pd.read_csv('\SDW\SDW2023.csv') # nomeou o Dataframe com um programa via pandas para ler o arquivo CSV(Tabela)
user_ids = df['UserID'].tolist() # criou variável chamando a coluna 'UsersID' na tabela referida com o método tolist()
# que devolve as informações solicitadas
print(user_ids) # [2689, 2693, 2694]

import requests  # A biblioteca "requests" é uma popular biblioteca Python que é amplamente utilizada para fazer chamadas HTTP 
# para interagir com recursos na web.
import json # A biblioteca "json" em Python é uma biblioteca padrão que fornece suporte para a serialização 
# (conversão de objetos Python em formato JSON) e desserialização (conversão de JSON em objetos Python) de dados

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app' # URL base da API que está hospedado no Swagger(endpoint)
def get_user(id): # funcao criada para recuperação do usuário
    response = requests.get(f'{sdw2023_api_url}/users/{id}') # aqui é utilizado o verbo htpp 'get' com a API de requests para 
    #solicitar os IDs dos usuários que estão no endpoit dentro de uma variável
    return response.json() if response.status_code == 200 else None # retornando funcao jason se o status code do dado solicitado
    # for 200, isto é, usuário criado com sucesso. Se não, retone nada

users = [user for id in user_ids if (user := get_user(id)) is not None] # list comprehension para percorrer cada userID
# se o usuário for não nulo na lista de users. Isso com base no resultado da função get_users
# se a busca for nula igonora-se
print(json.dumps(users, indent=2)) # imprimindo os usuários no formato json. 'indent' é para configurar identação;

openai_api_key = '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' # openAI key gerada

import openai # biblioteca openai 

openai.api_key = openai_api_key # chama a chave do openai API 

def generate_ai_news(user): # função para gerar mensagens de marketing personalizadas usando IA Generativa
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Você é um especialista em markting bancário."
        },
        {
            "role": "user",
            "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
        }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })

def update_user(user): # função para atualzar os usuários com os dados enriquecidos na API Santander Dev Week 23
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)  # definindo o response(resposta) para atualizar os dados
    # na API com o put informando o link e o id do usuário. O json= no final é para informar o corpo da requisição
    return True if response.status_code == 200 else False # se o response code for sucessivo retorne True, senão, False

for user in users: # percorrer os usuários para realizar o teste
    sucess = update_user(user) # variável criada com a função para validar a atualização dos dados dos users
    print(f"User {user['name']} updated? {sucess}") # 'User x Updated? True











