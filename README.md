# py-radar ⚽

Projeto pessoal de estudo em Python: consumo de API externa, backend com FastAPI e primeiros passos em frontend, acompanhando dados de futebol (tabela de campeonato e próximos jogos).

Usa a [API Futebol](https://www.api-futebol.com.br/).

## O que faz

- Mostra a tabela de classificação de um campeonato
- Mostra os próximos jogos de um time escolhido pelo usuário
- Trata erros comuns (time inválido, falha de conexão)
- Expõe os dados também via API própria (FastAPI)

> ⚠️ O plano gratuito da API usada só cobre o Brasileirão Série B. Em desenvolvimento, uso a chave de teste da API (dados fictícios) — troque pela chave de produção no `.env` pra dados reais.

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Crie um `.env` na raiz com:
```
API_KEY=sua_chave_aqui
```

Terminal:
```bash
python main.py
```

API:
```bash
uvicorn app:app --reload
```
Acesse `http://127.0.0.1:8000/docs`

---

Projeto em desenvolvimento, feito como parte do meu aprendizado de back-end.
<!-- Desenvolvido com apoio de tutoria por IA (Claude) -->
