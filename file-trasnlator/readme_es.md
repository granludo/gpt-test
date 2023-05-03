# gpt-traductor

Por Marc Alier @granludo https://wasabi.essi.upc.edu/ludo

Licenciado bajo la Licencia Pública General de GNU v3.0

Programa simple en Python 3 que utiliza el modelo GPT-3.5-turbo de OpenAI para traducir archivos de un idioma a otro. Divide el archivo en fragmentos de 20 líneas.

## requisitos

Necesitas tener una clave para usar la API de OpenAI, puedes obtener una aquí: https://beta.openai.com/docs/developer-quickstart/api-key este programa busca la clave en un archivo indicado en la variable "mykeypath" por defecto en la ruta '..//..//mykey.json'

Necesitas instalar los paquetes json y openai

> pip install openai
> pip install json

## uso

> python3 gpt-traductor.py archivo_origen idioma_origen idioma_destino archivo_destino**Ejemplo**

> python3 gpt-translate.py sample.md catalan italian sample_translated.md

Que te diviertas.