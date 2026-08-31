import os, dotenv, requests, json

# Carrega as variáveis do arquivo .env
dotenv.load_dotenv()

CHAVE = os.getenv("API_KEY")

def testar_conexao():
    url = "https://api.api-futebol.com.br/v1/me"
    headers = {"Authorization": "Bearer " + CHAVE}

    response = requests.get(url, headers=headers)
    data = response.json()
    print(json.dumps(data, indent=4, ensure_ascii=False)) # ORGANIZAR ESSA MERDA PRA EU CONSEGUIR LER PQP Q JSON HORRIVEL

def imprimir_bonito(dado):
    print(json.dumps(dado, indent=4, ensure_ascii=False))

def puxar_tabela(id):
    url = f"https://api.api-futebol.com.br/v1/campeonatos/{id}/tabela"
    headers = {"Authorization": "Bearer " + CHAVE}

    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# print(json.dumps(tabela(10), indent=4, ensure_ascii=False))