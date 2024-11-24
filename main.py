from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os
import json
from typing import Dict

app = FastAPI()

AGENTES_DIR = "agentes"  # Diretório onde os arquivos JSON estão armazenados

def carregar_dados_agente(nome_agente: str) -> Dict:
    file_path = os.path.join(AGENTES_DIR, f"{nome_agente}.json")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Agente '{nome_agente}' não encontrado.")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler os dados do agente: {e}")

@app.get("/")
def listar_agentes():
    agentes = [f.replace(".json", "") for f in os.listdir(AGENTES_DIR) if f.endswith(".json")]
    if not agentes:
        return JSONResponse(content={"message": "Nenhum agente encontrado."}, status_code=404)
    return {"agentes": agentes}

@app.get("/agentes/{nome_agente}")
def obter_dados_agente(nome_agente: str):
    dados = carregar_dados_agente(nome_agente)
    return dados
