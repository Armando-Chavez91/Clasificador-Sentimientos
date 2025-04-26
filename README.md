# Clasificador de Sentimientos en Tweets
Este proyecto implementa un sistema de clasificación de sentimientos basado en el algoritmo Naïve Bayes, entrenado desde cero y desplegado como una aplicación web utilizando Flask. Permite analizar textos cortos (tweets) y clasificarlos como positivo, negativo o neutro.

Instalación
Clona este repositorio o descarga los archivos del proyecto.

Asegúrate de tener instalado Python 3.0 en tu máquina.

Instala las dependencias necesarias ejecutando:

pip install -r requirements.txt

Ejecuta la aplicación localmente:

python app.py

Accede a la aplicación desde tu navegador en:

https://clasificador-sentimientos.onrender.com

Nota: Si deseas desplegarlo en Render.com, configura el Start Command como gunicorn app:app.

## Uso
Ingresa un texto o tweet en el campo de la página web.

Presiona el botón "Clasificar".

El sistema mostrará el sentimiento predicho: positivo, negativo o neutro.

## Arquitectura del Proyecto
El sistema está basado en una arquitectura de cliente-servidor:

Frontend (cliente):

Página web desarrollada en HTML, CSS y JavaScript.

Envía solicitudes POST con el texto ingresado.

Backend (servidor):

Aplicación Flask en Python que recibe los textos, limpia el contenido, aplica el modelo de Naïve Bayes y devuelve la predicción.

Motor de inferencia basado en el modelo entrenado modelo_naivebayes.pkl.

Despliegue:

Servicio web publicado en Render.com.

## Descripción de los Archivos
app.py: Código del servidor Flask que maneja el backend y motor de inferencia.

modelo_naivebayes.pkl: Modelo Naïve Bayes entrenado guardado en formato pickle.

requirements.txt: Lista de dependencias necesarias para ejecutar la aplicación.

templates/index.html: Archivo HTML que define la interfaz gráfica del usuario (Frontend).

static/style.css: Hoja de estilos CSS que da formato visual a la página web.

README.md: Documento de instalación, uso y estructura del proyecto.

## Tecnologías Utilizadas
Python 3

Flask (framework web)

gunicorn (servidor de aplicaciones para despliegue)

HTML5 (estructura de la página web)

CSS3 (diseño y estilos visuales)

Render.com (plataforma de despliegue en la nube)

Pickle (serialización del modelo entrenado)
