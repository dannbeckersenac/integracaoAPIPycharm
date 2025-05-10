import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY_CLIMA")

if not api_key:
    raise ValueError("API Key não encontrada nas variáveis de ambiente.")

def buscar_cidade(cidade):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "appid": api_key,
        "q": cidade,
        "lang": "pt_br",
        "units": "metric"
    }

    resposta = requests.get(url=url, params=params)

    status_code = resposta.status_code

    if status_code == 401:
        print("Erro. Chave API expirou ou é inválida.")
        quit()

    elif status_code == 404:
        return status_code, "Erro. Cidade não encontrada, tente novamente."

    elif status_code == 200:
        return status_code, resposta.json()

    else:
        return status_code, "Ocorreu algum erro desconhecido."

def extrair_temperatura(cidade):
    return cidade["temperatura"]

def menu():
    print("\nMenu de opções:")
    print("""
    0 - Sair
    1 - Buscar clima de cidades
    """)
    return input("Escolha uma opção: ")

while True:
    opcao = menu()
    
    if opcao == "0":
        break
    
    elif opcao == "1":

        try:
            quantidade_cidades = int(input("Digite a quantidade de cidades que deseja buscar (ao menos 2 e no máximo 5): "))
        except ValueError:
            print("Valor digitado não é um número. Tente novamente.")
            continue

        if quantidade_cidades < 2 or quantidade_cidades > 5:
            print("Valor digitado fora do intervalo. Tente novamente")
            continue

        cidades = []
        contador = 1
        while contador <= quantidade_cidades:
            cidade = input(f"Digite o nome da {contador}ª cidade: ")

            status_code, resultado = buscar_cidade(cidade)

            if status_code != 200:
                print(resultado)
                continue



            clima = resultado["weather"][0]["description"]
            temperatura = resultado["main"]["temp"]

            informacao_cidade = {
                "cidade": cidade,
                "clima": clima,
                "temperatura": temperatura
            }

            cidades.append(informacao_cidade)
            print(f"Cidade: {cidade}, o clima é {clima} com temperatura de {temperatura}ºC.")
            contador += 1

        cidades_ordenadas = sorted(cidades, key=extrair_temperatura, reverse=True)

        cidade_mais_quente = cidades_ordenadas[0]

        print(f"A cidade de maior temperatura é {cidade_mais_quente['cidade']}, com {cidade_mais_quente['temperatura']}ºC.")
        
    else:
        print("Opção não é válida. Tente novamente.")
        continue