import time
import datetime as dt


if __name__ == "__main__":
    print("🚀 Iniciando aplicação Python dentro do container...")
    count = 0
    while True:
        count += 1
        print(f"[{dt.datetime.now().isoformat()}] Execução #{count} dentro do container 🐳")
        time.sleep(2)