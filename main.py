import requests


def atualizar_post(codigo):
    url = f"https://jsonplaceholder.typicode.com/posts/{codigo}"

    novo_post = {
        "title": "Outro titulo",
    }

    resposta = requests.patch(url, json=novo_post)
    print(resposta.status_code)
    resultado_api = resposta.json()
    print(resultado_api)


def visualizar_post(codigo):
    url = f"https://jsonplaceholder.typicode.com/posts/{codigo}"
    resposta = requests.get(url)
    print(resposta.status_code)
    resultado_api = resposta.json()
    print(resultado_api)


visualizar_post(1)
atualizar_post(1)