from fastapi import FastAPI
from api.football_api import puxar_tabela, puxar_proximos_jogos
from datetime import datetime
from times import TIMES


app = FastAPI()

@app.get("/tabela/{campeonato_id}")
def rota_tabela(campeonato_id):
    return puxar_tabela(campeonato_id)

@app.get("/proximos-jogos/{time_id}")
def rota_proximos(time_id):
    return puxar_proximos_jogos(time_id)