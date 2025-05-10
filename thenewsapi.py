import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY_NEWS")

if not api_key:
    raise ValueError("API Key não encontrada nas variáveis "
                     "de ambiente.")

url = "https://newsapi.org/v2/everything"

headers = {
    'X-Api-Key': api_key
}

params = {
    'q': "tecnologia",
    'language': "pt",
    'page': 2
}

resposta = requests.get(url=url, headers=headers, params=params)
print(resposta.status_code)

resposta_json = resposta.json()

#print("Site da notícia de posição 7:", resposta_json["articles"][7]["source"]["name"])

for artigo in resposta_json["articles"][:10]:
    print("\n")
    print(artigo["title"])
    print(artigo["description"])
    print(artigo["url"])

