from flask import Flask, Response
import random  # <--- importar random

app = Flask(__name__)

@app.route('/custom-metrics')
def custom_metrics():
    # Generar un valor aleatorio entre 0 y 100
    random_value = random.randint(0, 100)

    # Custom metrics en formato Prometheus
    metrics_data = f"""
# HELP my_custom_metric A custom metric example.
# TYPE my_custom_metric counter
my_custom_metric {random_value}
"""
    return Response(metrics_data, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
    time.sleep(0.5)
