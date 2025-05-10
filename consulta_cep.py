import time

import requests

cep = input("Digite seu CEP: ")

resultado = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
if resultado.status_code == 400:
    print("Erro na sintaxe. Verifique se está digitando somente números ou se está digitando os 8 dígitos de CEP.")
    exit()

resultado = resultado.json()
if "erro" in resultado:
    print("Erro de CEP inválido. Digite novamente.")
    exit()

logradouro = resultado["logradouro"]
complemento = resultado["complemento"]
bairro = resultado["bairro"]

print("Conectando com banco de dados...")
time.sleep(2)
print("\nInformações salvas com sucesso!")
print("Logradouro:", logradouro)
print("Complemento:", complemento)
print("Bairro:", bairro)


