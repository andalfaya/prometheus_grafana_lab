from prometheus_client import start_http_server, Summary, Counter
import random
import time

# --- Métricas ---
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count_total', 'Total number of requests')

# --- Función de procesamiento simulada ---
@REQUEST_TIME.time()
def process_request(t):
    time.sleep(t)
    REQUEST_COUNT.inc()

if __name__ == '__main__':
    # Exponer métricas en el puerto 8000
    start_http_server(8000)
    print("Python Exporter corriendo en http://localhost:8000/metrics")

    while True:
        # Simular entre 5 y 10 requests por ciclo con tiempos aleatorios
        for _ in range(random.randint(5, 10)):
            process_request(random.random())  # tiempo entre 0 y 1s
        time.sleep(0.5)  # pequeña pausa entre ciclos
