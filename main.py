from api.football_api import puxar_tabela, imprimir_bonito #vai na pasta api -> acessa o arquivo football_api -> pega a função tabela de lá

#imprimir_bonito(puxar_tabela(10))

def tabela():
    resultado = puxar_tabela(10) # puxa a tabela com o id = 10 (Série A BR)
    print("\n|  --- Campeonato Brasileiro ---\n|")
    for time in resultado:
        print(f"| {time['posicao']}º - {time['time']['nome_popular']} - {time['pontos']} pts")

tabela()