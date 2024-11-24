import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

AGENTES_DIR = "agentes"  # Diretório onde os arquivos JSON serão armazenados

# Configuração do Selenium WebDriver
def configurar_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service("C:/caminho/para/chromedriver.exe"), options=options)
    return driver

# Função para capturar os dados de um agente
def capturar_dados(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    try:
        effort_points = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "character-stream-pe-value"))).text
        sanity_points = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "character-stream-bar-value-san"))).text
        health_points = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "character-stream-bar-value-pv"))).text
        agent_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "character-stream-profile-name"))).text
        return {
            "effort_points": effort_points,
            "sanity_points": sanity_points,
            "health_points": health_points,
            "agent_name": agent_name,
        }
    except Exception as e:
        print(f"Erro ao capturar dados do URL {url}: {e}")
        return None

# Salvar os dados do agente em um arquivo JSON
def salvar_dados(nome, dados):
    if not os.path.exists(AGENTES_DIR):
        os.makedirs(AGENTES_DIR)
    with open(os.path.join(AGENTES_DIR, f"{nome}.json"), "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# Função principal para monitorar e atualizar os agentes periodicamente
def monitorar_agentes(intervalo=60):
    agentes = [
        ("Skiy", "https://crisordemparanormal.com/agente/stream/VDUU6qfqHMJPSbiAaFc9"),
        ("Tony", "https://crisordemparanormal.com/agente/stream/Jlqf3zlMi7EG1S5RSDPf"),
    ]
    driver = configurar_driver()
    try:
        while True:
            for nome, url in agentes:
                dados = capturar_dados(driver, url)
                if dados:
                    salvar_dados(nome, dados)
            time.sleep(intervalo)  # Atualiza a cada `intervalo` segundos
    except KeyboardInterrupt:
        print("Monitoramento interrompido.")
    finally:
        driver.quit()

if __name__ == "__main__":
    monitorar_agentes()
