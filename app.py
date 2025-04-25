from flask import Flask, request, jsonify, render_template
import pickle
import math
import re
import string

app = Flask(__name__)

# --- Cargar el modelo ---
with open('modelo_naivebayes.pkl', 'rb') as f:
    modelo = pickle.load(f)

# --- Función de limpieza ---
def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"http\S+", "", texto)
    texto = re.sub(r"@\w+", "", texto)
    texto = re.sub(r"#\w+", "", texto)
    texto = re.sub(rf"[{re.escape(string.punctuation)}]", "", texto)
    texto = re.sub(r"\d+", "", texto)
    return texto.split()

# --- Clasificador con neutro como fallback ---
def predecir(texto, modelo, umbral=0.05):
    palabras = limpiar_texto(texto)
    palabras_utiles = [p for p in palabras if p in modelo['vocabulario']]

    if len(palabras_utiles) == 0:
        return "neutro"

    scores = {}
    for clase in modelo['prob_clases']:
        log_prob = math.log(modelo['prob_clases'][clase])
        total = modelo['total_palabras'][clase]
        conteo = modelo['conteo_palabras'][clase]
        vocabulario = modelo['vocabulario']

        for palabra in palabras_utiles:
            frecuencia = conteo.get(palabra, 0)
            prob = (frecuencia + 1) / (total + len(vocabulario))
            log_prob += math.log(prob)

        scores[clase] = log_prob

    pos = scores.get("positivo", float('-inf'))
    neg = scores.get("negativo", float('-inf'))

    if abs(pos - neg) < math.log(1 + umbral):
        return "neutro"
    return "positivo" if pos > neg else "negativo"

# --- Ruta principal con frontend ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Ruta POST para clasificar texto ---
@app.route('/clasificar', methods=['POST'])
def clasificar():
    data = request.get_json()
    texto = data.get('texto', '')
    if not texto.strip():
        return jsonify({'error': 'Texto vacío'}), 400
    resultado = predecir(texto, modelo)
    return jsonify({'sentimiento': resultado})

# --- Ejecutar en entorno local (no se usa en Render) ---
if __name__ == '__main__':
    app.run()
