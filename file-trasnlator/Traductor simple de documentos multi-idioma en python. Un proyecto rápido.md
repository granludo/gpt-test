---
title: "Traductor simple de documentos multi-idioma en python. Un proyecto rápido."
date: 2023-04-08T02:01:58+05:30
description: "En esta entrada presento un pequeño proyecto que he publicado como open source.  Lo que hantes hubiera sido un proyecto de múchos años y varios millones de euros, ahora es una pequeña prueba hecha un sabado por la mañana. Las claves son Github Copilot, ChatGPT 4 como asistenes de programación y la API de GPT.3.5 turbo."
tags: [Castellano, Code, IA, ChatGPT]
---

En esta entrada presento un pequeño proyecto que he publicado como open source.  Lo que hantes hubiera sido un proyecto de múchos años y varios millones de euros, ahora es una pequeña prueba hecha un sabado por la mañana. Las claves son Github Copilot, ChatGPT 4 como asistenes de programación y la API de GPT.3.5 turbo.

![GPT-Transltate screenshoot](IMGS/GPT-Transtlator-screenshot.png)
# gpt-translator

Lo puedes descargar de https://github.com/granludo/gpt-test/tree/main/file-trasnlator 
  

Licenciado bajo la Licencia Pública General de GNU v3.0
  

Programa simple en Python 3 que utiliza el modelo GPT-3.5-turbo de OpenAI para traducir archivos de un idioma a otro. Divide el archivo en fragmentos de 20 líneas.
  
## Requisitos

Necesitas tener una clave para usar la API de OpenAI, puedes obtener una aquí: https://beta.openai.com/docs/developer-quickstart/api-key este programa busca la clave en un archivo indicado en la variable "mykeypath" por defecto en la ruta '..//..//mykey.json'

Necesitas tener instalado Python 3 en tu sistema. Yo he usado python 3.10 

Necesitas instalar los paquetes json y openai

> pip install openai

> pip install json

Quizás en tu sistema debas usar pip3 en vez de pip.

## Uso

> python3 gpt-traductor.py archivo_origen idioma_origen idioma_destino archivo_destino**Ejemplo**


> python3 gpt-translate.py sample.md catalan italian sample_translated.md
  

Que te diviertas.
