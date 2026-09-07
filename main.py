from api.football_api import imprimir_bonito, puxar_tabela, puxar_proximos_jogos
from datetime import datetime #vai na pasta api -> acessa o arquivo football_api -> pega a função tabela de lá
from times import TIMES

def inicio():
    nome_time = str(input("[!] Qual seu clube de futebol nacional favorito?\n-> ")).lower().strip()
    try:
        time_id = TIMES[nome_time]
        proximos_jogos(time_id)
    except KeyError:
        print("Clube inserido inexistente. Tente novamente.")

def tabela():
    resultado = puxar_tabela(10) # puxa a tabela com o campeonato_id = 10 (Série A BR)
    print("\n|  --- Campeonato Brasileiro ---\n|")
    for time in resultado:
        # :<15 -> alinha à esquerda, largura mínima N (15). reserva 15 caracteres pra esse valor, se sobrar, preenche com espaço branco
        print(f"| {time['posicao']:<3}º - {time['time']['nome_popular']:<14} - {time['pontos']} pts   ID: {time['time']['time_id']}")

def proximos_jogos(time_id):
    jogos = puxar_proximos_jogos(time_id)
    print(f"\n|   --- Próximos Jogos ---\n|")

    contador = 0

    for campeonato_slug, lista_partidas in jogos.items():           # campeonato_slug é tipo "campeonato-brasileiro" | lista_partidas é a LISTA de jogos daquele campeonato
        for jogo in lista_partidas:                                 # aqui, jogo é UM dicionário de partida (com placar, status, etc)
            if jogo['data_realizacao_iso']:
                data_obj = datetime.fromisoformat(jogo['data_realizacao_iso'])
                data = data_obj.strftime("%d/%m/%Y - %H:%M")
            else:
                data = "a definir"

            campeonato_nome = campeonato_slug.replace("-", " ")
           
            print(f"┌─────────────────────────────")
            print(f"│    {data}")
            print(f"│ {jogo['placar']}")
            print(f"│   {campeonato_nome}")     
            print(f"└─────────────────────────────")

            contador += 1
            if contador >= 5: #mostra os 5 primeiros jogos
                return

tabela()
inicio()