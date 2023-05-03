títol: "Traductor simple de documents multi-idioma en python. Un projecte ràpid."
data: 2023-04-08T02:01:58+05:30
descripció: "En aquesta entrada presento un petit projecte que he publicat com a open source. El que abans hauria estat un projecte de molts anys i diversos milions d'euros, ara és una petita prova feta un dissabte al matí. Les claus són Github Copilot, ChatGPT 4 com a assistents de programació i l'API de GPT.3.5 turbo."
etiquetes: [Castellà, Code, IA, ChatGPT]

En aquesta entrada presento un petit projecte que he publicat com a open source. El que abans hauria estat un projecte de molts anys i diversos milions d'euros, ara és una petita prova feta un dissabte al matí. Les claus són Github Copilot, ChatGPT 4 com a assistents de programació i l'API de GPT.3.5 turbo.

![Captura de pantalla de GPT-Translate](IMGS/GPT-Transtlator-screenshot.png)
# gpt-translator

El pots descarregar de https://github.com/granludo/gpt-test/tree/main/file-trasnlator


Llicenciat sota la Llicència Pública General de GNU v3.0


Programa simple en Python 3 que utilitza el model GPT-3.5-turbo d'OpenAI per traduir fitxers d'un idioma a un altre. Divideix el fitxer en fragments de 20 línies.## Requisits

Necessites tenir una clau per usar l'API d'OpenAI, pots obtenir-ne una aquí: https://beta.openai.com/docs/developer-quickstart/api-key aquest programa busca la clau en un fitxer indicat a la variable "mykeypath" per defecte en la ruta '..//..//mykey.json'

Necessites tenir instal·lat Python 3 al teu sistema. Jo he usat python 3.10

Necessites instal·lar els paquets json i openai

> pip install openai

> pip install json

Potser al teu sistema hauràs d'usar pip3 en lloc de pip.

## Ús

> python3 gpt-traductor.py fitxer_origen idioma_origen idioma_destí fitxer_destí**Exemple**

> python3 gpt-translate.py sample.md català italià sample_translated.mdQue et diverteixis.