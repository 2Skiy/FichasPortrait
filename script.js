async function fetchCharacterData() {
    try {
        const response = await fetch("https://crisordemparanormal.com/agente/stream/VDUU6qfqHMJPSbiAaFc9");
        const html = await response.text();

        // Parse o HTML recebido
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");

        // Extração de dados dinâmicos
        const nome = doc.querySelector('.character-stream-profile-name')?.innerText || "Não encontrado";
        const sanidade = doc.querySelector('.character-stream-bar-value-san')?.innerText || "Não encontrado";
        const vida = doc.querySelector('.character-stream-bar-value-pv')?.innerText || "Não encontrado";
        const esforco = doc.querySelector('.character-stream-pe-value')?.innerText || "Não encontrado";
        const foto = doc.querySelector('.character-stream-profile-picture')?.src || "";

        // Atualizar o DOM com os dados
        document.getElementById("nome").textContent = nome;
        document.getElementById("sanidade").textContent = sanidade;
        document.getElementById("vida").textContent = vida;
        document.getElementById("esforco").textContent = esforco;
        document.getElementById("foto").src = foto;
    } catch (error) {
        console.error("Erro ao buscar os dados:", error);
    }
}

// Atualizar os dados a cada 5 segundos
setInterval(fetchCharacterData, 5000);
fetchCharacterData();
