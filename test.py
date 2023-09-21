import pandas as pd
import openai

# Carregar o arquivo CSV
data = pd.read_csv('D:\SDW\dados_projeto.csv')

# Definir a chave da API do OpenAI
chave_openAI = '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'
openai.api_key = chave_openAI

def gerador_msg(user, name, age, city):
    mensagens = []
    for i in range(len(user)):
        mensagem = f"Crie uma mensagem para {name[i]} sobre atrações turísticas na cidade {city[i]} considerando a faixa etária {age[i]} de cada um deles (máximo de 100 caracteres)"
        mensagens.append({"role": "user", "content": mensagem})

        # Adicionar mensagem de sistema
        mensagens.append({"role": "system", "content": "Você é um especialista em turismo"})

        # Gerar a resposta do modelo
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=mensagens
        )

        resposta = completion.choices[0].message.content.strip('\"')

        # Limpar a lista de mensagens para o próximo usuário
        mensagens = []

        # Imprimir a resposta para o usuário atual
        print(f"Para o usuário {user[i]}:\n{resposta}\n")

# Obtém as listas de dados
user = data['UserID'].tolist()
name = data['Name'].tolist()
age = data['Age'].tolist()
city = data['City'].tolist()

# Chamada da função para gerar mensagens
gerador_msg(user, name, age, city)

