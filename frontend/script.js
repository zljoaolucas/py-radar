const API_URL = "http://127.0.0.1:8000";

// Troque para 14 quando estiver usando a chave de PRODUÇÃO
// (o plano gratuito só libera a Série B, campeonato_id = 14).
// Com a chave de TESTE, use 10 (Brasileirão A, dado fictício de demonstração).
const CAMPEONATO_ID = 14;

let timeSelecionadoId = null;

// Carrega a tabela assim que a página abre, e usa os mesmos dados
// pra montar os escudos clicáveis dos times.
window.addEventListener("DOMContentLoaded", carregarTabela);

// ---------- TABELA ----------

async function carregarTabela() {
    const container = document.getElementById("tabela-resultado");

    try {
        const resposta = await fetch(`${API_URL}/tabela/${CAMPEONATO_ID}`);
        const times = await resposta.json();
        renderizarTabela(times);
        renderizarSeletorTimes(times);
    } catch (erro) {
        container.innerHTML = `<p class="mensagem-erro">Não consegui carregar a tabela. Confirme se a API está rodando.</p>`;
    }
}

function renderizarTabela(times) {
    const container = document.getElementById("tabela-resultado");
    container.innerHTML = "";

    for (const time of times) {
        const linha = document.createElement("div");
        linha.className = "linha-time" + (time.posicao <= 4 ? " top4" : "");
        linha.innerHTML = `
            <span class="posicao">${time.posicao}</span>
            <span class="nome-time">${time.time.nome_popular}</span>
            <span class="pontos">${time.pontos} pts</span>
        `;
        container.appendChild(linha);
    }
}

// ---------- SELETOR DE TIMES (escudos, gerados a partir da tabela) ----------

function renderizarSeletorTimes(times) {
    const container = document.getElementById("seletor-times");
    container.innerHTML = "";

    // mostra só os 8 primeiros colocados, pra não lotar a tela
    const principais = times.slice(0, 8);

    for (const item of principais) {
        const time = item.time;
        const botao = document.createElement("button");
        botao.className = "time-botao";
        botao.dataset.timeId = time.time_id;

        const imagem = time.escudo
            ? `<img src="${time.escudo}" alt="${time.nome_popular}">`
            : `<div class="iniciais">${time.sigla || "?"}</div>`;

        botao.innerHTML = `
            ${imagem}
            <span class="nome">${time.nome_popular}</span>
        `;

        botao.addEventListener("click", () => selecionarTime(time.time_id, botao));
        container.appendChild(botao);
    }
}

function selecionarTime(timeId, botaoClicado) {
    timeSelecionadoId = timeId;

    document.querySelectorAll(".time-botao").forEach((b) => b.classList.remove("ativo"));
    botaoClicado.classList.add("ativo");

    buscarProximosJogos(timeId);
}

// ---------- PRÓXIMOS JOGOS ----------

async function buscarProximosJogos(timeId) {
    const container = document.getElementById("jogos-resultado");
    container.innerHTML = `<p class="carregando">Carregando jogos...</p>`;

    try {
        const resposta = await fetch(`${API_URL}/proximos-jogos/${timeId}`);
        const dados = await resposta.json();
        renderizarJogos(dados);
    } catch (erro) {
        container.innerHTML = `<p class="mensagem-erro">Não consegui carregar os jogos. Confirme se a API está rodando.</p>`;
    }
}

function renderizarJogos(jogosPorCampeonato) {
    const container = document.getElementById("jogos-resultado");
    container.innerHTML = "";

    let contador = 0;
    const limite = 5;

    for (const campeonatoSlug in jogosPorCampeonato) {
        const partidas = jogosPorCampeonato[campeonatoSlug];

        for (const jogo of partidas) {
            if (contador >= limite) return;

            const data = jogo.data_realizacao_iso
                ? new Date(jogo.data_realizacao_iso).toLocaleString("pt-BR", {
                    day: "2-digit",
                    month: "2-digit",
                    year: "numeric",
                    hour: "2-digit",
                    minute: "2-digit",
                })
                : "a definir";

            const cartao = document.createElement("div");
            cartao.className = "cartao-jogo";
            cartao.innerHTML = `
                <div class="data">${data}</div>
                <div class="placar">${jogo.placar}</div>
                <div class="campeonato">${campeonatoSlug.replace(/-/g, " ")}</div>
            `;
            container.appendChild(cartao);

            contador++;
        }
    }

    if (contador === 0) {
        container.innerHTML = `<p class="mensagem-vazia">Nenhum jogo encontrado pra esse time.</p>`;
    }
}