const API_URL = "https://seuservidor.com/dados.json"; // Substitua pelo endereço da sua API hospedada

async function carregarDados() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Erro ao buscar dados: ${response.status}`);
        }

        const data = await response.json();
        exibirDados(data);
    } catch (error) {
        console.error("Erro ao carregar os dados:", error);
        document.getElementById("agentes").innerHTML = `<p>Erro ao carregar os dados.</p>`;
    }
}

function exibirDados(data) {
    const agentesDiv = document.getElementById("agentes");
    agentesDiv.innerHTML = "";

    Object.keys(data).forEach((key) => {
        const valor = data[key];
        const elemento = document.createElement("p");
        elemento.textContent = `${key}: ${valor}`;
        agentesDiv.appendChild(elemento);
    });
}

// Atualiza os dados a cada 5 segundos
setInterval(carregarDados, 5000);
carregarDados();
