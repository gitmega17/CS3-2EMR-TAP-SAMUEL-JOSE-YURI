import requests
import random
import time
import os
from dotenv import load_dotenv


load_dotenv()
url = os.getenv('BACKEND_URL', 'http://127.0.0.1:5000/dados-sensores')
token = os.getenv("JWT_TOKEN")

# Cabeçalhos da requisição, incluindo o token de autenticação
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# Função para simular os dados do sensor e enviar para o backend
def simular_sensores():
    while True:
        # Gerando dados aleatórios para os sensores
        sensor_id = random.choice([1, 2]) 
        temperatura = round(random.uniform(20.0, 30.0), 2)  # Temperatura entre 20.0 e 30.0 graus Celsius
        umidade = round(random.uniform(40.0, 70.0), 2)  # Umidade entre 40% e 70%

        # Criando o objeto de dados
        dados = {
            "sensor_id": sensor_id,
            "temperatura": temperatura,
            "umidade": umidade
        }

        try:
            # Enviando os dados para o backend com o token de autenticação no cabeçalho
            response = requests.post(url, json=dados, headers=headers)
            # Verificando se a resposta foi bem-sucedida
            if response.status_code == 201:
                print(f'Dados enviados com sucesso: {dados}')
            else:
                print(f'Erro ao enviar os dados: {response.status_code}, {response.text}')
        except requests.exceptions.RequestException as e:
            print(f'Erro de conexão: {e}')

        # Aguarda 10 segundos antes de enviar os próximos dados
        time.sleep(5)

if __name__ == "__main__":
    simular_sensores()
