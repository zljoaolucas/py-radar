import os, dotenv, requests, json

# Carrega as variáveis do arquivo .env
dotenv.load_dotenv()

CHAVE = os.getenv("API_KEY")

def fazer_requisicao(url):
    headers = {"Authorization": "Bearer "+ CHAVE}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        print("Erro ao conectar com a API. Verifique sua internet.")
        return {}

def testar_conexao():
    url = "https://api.api-futebol.com.br/v1/me"
    headers = {"Authorization": "Bearer " + CHAVE}

    response = requests.get(url, headers=headers)
    data = response.json()
    print(json.dumps(data, indent=4, ensure_ascii=False)) # ORGANIZAR ESSA MERDA PRA EU CONSEGUIR LER PQP Q JSON HORRIVEL

def imprimir_bonito(dado):
    print(json.dumps(dado, indent=4, ensure_ascii=False))

def puxar_tabela(campeonato_id):
    url = f"https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/tabela"
    return fazer_requisicao(url)

def puxar_proximos_jogos(time_id):
    url = f"https://api.api-futebol.com.br/v1/times/{time_id}/partidas/proximas"
    return fazer_requisicao(url)