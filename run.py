import threading
from subprocess import Popen
import os

# Executar o script de coleta
def iniciar_coletor():
    os.system("python coletor.py")

# Executar o servidor FastAPI
def iniciar_servidor():
    os.system("uvicorn main:app --host 0.0.0.0 --port 8000 --reload")

if __name__ == "__main__":
    thread_coletor = threading.Thread(target=iniciar_coletor)
    thread_servidor = threading.Thread(target=iniciar_servidor)

    thread_coletor.start()
    thread_servidor.start()

    thread_coletor.join()
    thread_servidor.join()
